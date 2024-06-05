from venv import logger
import tiktoken
import json
import re
import codecs
import time
from kph.src.parse.parse import parse_doc
from kph.src.common.taxonomy import (
    agencies_dict,
    regions_dict,
    industries_dict,
    partners_involved_dict,
    capabilities_services_dict,
)
from kph.src.parse.prompts import summarize_system_message, summarize_user_message
from kph.src.common.llm_clients import (
    openai_client,
    azure_openai_client_gpt4,
    azure_openai_client_gpt35_16k,
    anyscale_client,
    groc_client,
)


def process_json_str(json_str):

    json_str = json_str.replace("```json", "").replace("```", "").strip()

    try:
        parsed_json = json.loads(json_str, strict=False)
        return parsed_json

    except json.JSONDecodeError:
        try:
            parsed_json = json.loads(json_str.decode("utf-8"), ensure_ascii=False)
            print("JSON string paresed after decoding utf-8.")
            return parsed_json
        except json.JSONDecodeError:
            try:
                decoded_bytes, _ = codecs.escape_decode(json_str)
                # Now decode the bytes to a string and try to parse the JSON again
                fixed_json_string = decoded_bytes.decode("utf-8")
                parsed_json = json.loads(fixed_json_string, ensure_ascii=False)
                print(
                    "JSON string paresed after decoding escape characters using codecs."
                )
                return parsed_json
            except json.JSONDecodeError:
                # Define a regular expression pattern to match "key": `value` pairs
                pattern = r'"([^"]+)": `((?:[^`\\]|\\.)*)`'
                print("Correcting invalid JSON string...")

                def replace_match(match):
                    key = match.group(1)
                    value = (
                        match.group(2)
                        .replace('"', r"\"")
                        .replace("\\`", r"`")
                        .replace("\n", r"\n")
                    )  # Replace " with \" and \` with `
                    return f'"{key}": "{value}"'

                # Use re.sub to replace all matches in the input string
                replaced_string = re.sub(pattern, replace_match, json_str)

                try:
                    # Attempt to parse the modified string as JSON
                    parsed_json = json.loads(replaced_string, strict=False)
                    print(
                        "JSON string was fixed after replacing escape charachters manually."
                    )
                    return parsed_json
                except json.JSONDecodeError:
                    raise ValueError(
                        f"Input string was invalid JSON, and we weren't able to fix it. We tried converting:\n\t{json_str}\n\n...to...\n\t{replaced_string}"
                    )


def num_tokens_from_string(string: str, model_name: str = "gpt-4") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def summarize(doc, model_name: str = "gpt-4", max_tokens=2000, temperature=0.0):

    system_message = summarize_system_message.format(
        agencies_dict=json.dumps(agencies_dict, indent=4),
        regions_dict=json.dumps(regions_dict, indent=4),
        industries_dict=json.dumps(industries_dict, indent=4),
        partners_involved_dict=json.dumps(partners_involved_dict, indent=4),
        capabilities_services_dict=json.dumps(capabilities_services_dict, indent=4),
    )

    user_message = summarize_user_message.format(
        doc_file_metadata=json.dumps(doc["doc_file_metadata"], indent=4),
        doc_text_unstructured=doc["doc_text_unstructured"],
    )

    num_tokens = num_tokens_from_string(user_message)
    print(f"Number of tokens in the prompt: {num_tokens}")

    if model_name == "mixtral-8x7b-32768":
        print("Using Groc client for model: ", model_name)
        response = groc_client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            seed=42,
            n=1,
        )

    elif model_name in ("gpt-4-turbo", "gpt-4-0125-preview", "gpt-4o"):
        print("Using OpenAI client for model: ", model_name)
        response = openai_client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            seed=42,
            n=5,
        )

    elif model_name == "gpt-35-turbo-16k":
        if num_tokens < 14_000:
            print("Using Azure OpenAI client for model: ", model_name)
            response = azure_openai_client_gpt35_16k.chat.completions.create(
                model="gpt-35-turbo-16k",
                messages=[
                    {
                        "role": "system",
                        "content": system_message,
                    },
                    {
                        "role": "user",
                        "content": user_message,
                    },
                ],
                max_tokens=max_tokens,
                temperature=temperature,
                seed=42,
                # logprobs=5,
                # response_format={ "type": "json_object" }
            )
        else:
            raise ValueError(
                f"Number of tokens in the prompt is {num_tokens}, which is more than the allowed limit of 14k tokens."
            )

    elif model_name in (
        "meta-llama/Meta-Llama-3-70B-Instruct",
        "mistralai/Mixtral-8x22B-Instruct-v0.1",
    ):
        print("Using Anyscale client for model: ", model_name)
        response = anyscale_client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            seed=42,
            n=1,
            # logprobs=5,
            # response_format={ "type": "json_object" }
        )

    else:  # model_name == "gpt-4"
        if num_tokens < 30_000:
            print("Using Azure OpenAI client for model: ", model_name)
            response = azure_openai_client_gpt4.chat.completions.create(
                model=model_name,
                messages=[
                    {
                        "role": "system",
                        "content": system_message,
                    },
                    {
                        "role": "user",
                        "content": user_message,
                    },
                ],
                max_tokens=max_tokens,
                temperature=temperature,
                seed=42,
                n=5,
                # logprobs=5,
                # response_format={ "type": "json_object" }
            )
        else:
            raise ValueError(
                f"Number of tokens in the prompt is {num_tokens}, which is more than the allowed limit of 32k tokens."
            )

    return response


def extract_serializable_response(response):
    # Extract all fields of the response in a serializable format
    try:
        return {
            "id": response.id,
            "choices": [
                {
                    "finish_reason": choice.finish_reason,
                    "index": choice.index,
                    "logprobs": choice.logprobs,
                    "message": {
                        "content": process_json_str(choice.message.content),
                        "role": choice.message.role,
                        "function_call": getattr(choice.message, "function_call", None),
                        "tool_calls": choice.message.tool_calls,
                    },
                    "finish_reason": choice.finish_reason,
                }
                for choice in response.choices
            ],
            "created": response.created,
            "model": response.model,
            "object": response.object,
            "system_fingerprint": response.system_fingerprint,
            "usage": {
                "completion_tokens": response.usage.completion_tokens,
                "prompt_tokens": response.usage.prompt_tokens,
                "total_tokens": response.usage.total_tokens,
            },
            "prompt_filter_results": getattr(response, "prompt_filter_results", None),
        }
    except Exception as e:
        return {"error": "Invalid response structure." + str(e)}


def summarize_case_study(
    filename: str, max_retries=3, delay_between_retries=2, model_name="gpt-4"
):

    doc = parse_doc(filename)

    retries = 0
    while retries < max_retries:
        try:
            # Describe the image using your function
            response = summarize(doc, model_name=model_name)
            print(f"LLM response:\n {response}")
            serializable_response = extract_serializable_response(response)
            doc["doc_extracted_metadata"] = serializable_response["choices"][0][
                "message"
            ]["content"]
            return doc, serializable_response

        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")
            print(f"{response=}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying... Attempt {retries + 1}/{max_retries}")
                time.sleep(delay_between_retries)
            else:
                print(f"Max retries reached for {filename}. Moving to next file.")

    return None, None
