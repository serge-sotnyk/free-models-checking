# free-models-checking
Smoke-test for free models

It is a small test for providers that give access to use LLMs for free.

How to use:

1. install requirements.txt (better into virtual environment)
2. create .env file with API keys (use .env.example as a template)
3. run `python models_tester.py`
4. run `python models_tester_litellm.py`

Below we can see the results on the 2024-11-02 (YYYY-MM-DD) date.

## Light-llm test:
=== Results for github/gpt-4o ===

Model: github/gpt-4o

Summarization test:
Failed: litellm.APIError: APIError: GithubException - Error code: 413 - {'error': {'code': 'tokens_limit_reached', 'message': 'Request body too large for gpt-4o model. Max size: 8000 tokens.', 'details': 'Request body too large for gpt-4o model. Max size: 8000 tokens.'}}

Tool usage test:
Result: ModelResponse(id='chatcmpl-APFAuNKdN5DPyifzjF7LObXZaJ3tJ', choices=[Choices(finish_reason='tool_calls', index=0, message=Message(content="To solve the mathematical expression \\(1234568789 \\times 9878654321\\), we can directly utilize the `multiply` tool to compute the result. Here's how it can be done:\n\n1. Identify the multiplicands: \\(a = 1234568789\\) and \\(b = 9878654321\\).\n\n2. Use the `multiply` tool with these values to get the result of the multiplication.\n\nNow, let's perform the multiplication using the tool.", role='assistant', tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"a":1234568789,"b":9878654321}', name='multiply'), id='call_gqo3AbRQnsd8iaDCbPSo2dir', type='function')], function_call=None))], created=1730579896, model='github/gpt-4o-2024-08-06', object='chat.completion', system_fingerprint='fp_d54531d9eb', usage=Usage(completion_tokens=121, prompt_tokens=76, total_tokens=197, completion_tokens_details=None, prompt_tokens_details=None), service_tier=None)

=== Results for github/gpt-4o-mini ===

Model: github/gpt-4o-mini

Summarization test:
Failed: litellm.APIError: APIError: GithubException - Error code: 413 - {'error': {'code': 'tokens_limit_reached', 'message': 'Request body too large for gpt-4o-mini model. Max size: 8000 tokens.', 'details': 'Request body too large for gpt-4o-mini model. Max size: 8000 tokens.'}}

Tool usage test:
Result: ModelResponse(id='chatcmpl-APFAwqRU0iHurY4BaUuGHstiE7fel', choices=[Choices(finish_reason='tool_calls', index=0, message=Message(content=None, role='assistant', tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"a":1234568789,"b":9878654321}', name='multiply'), id='call_soCDsc4JTulTkLK1kNVGgxNA', type='function')], function_call=None))], created=1730579898, model='github/gpt-4o-mini', object='chat.completion', system_fingerprint='fp_d54531d9eb', usage=Usage(completion_tokens=23, prompt_tokens=76, total_tokens=99, completion_tokens_details=None, prompt_tokens_details=None), service_tier=None)

=== Results for github/Meta-Llama-3.1-405B-Instruct ===

Model: github/Meta-Llama-3.1-405B-Instruct

Summarization test:
Failed: litellm.APIError: APIError: GithubException - Error code: 413 - {'error': {'code': 'tokens_limit_reached', 'message': 'Request body too large for meta-llama-3.1-405b-instruct model. Max size: 8000 tokens.', 'details': 'Request body too large for meta-llama-3.1-405b-instruct model. Max size: 8000 tokens.'}}

Tool usage test:
Result: ModelResponse(id='562adb53-688f-4ada-95ed-d35a3fee9d2f', choices=[Choices(finish_reason='stop', index=0, message=Message(content='{"name": "multiply", "parameters": {"a": "1234568789", "b": "9878654321"}}<|eom_id|>', role='assistant', tool_calls=None, function_call=None))], created=1730579900, model='github/Meta-Llama-3-405B-Instruct', object='chat.completion', system_fingerprint=None, usage=Usage(completion_tokens=29, prompt_tokens=221, total_tokens=250, completion_tokens_details=None, prompt_tokens_details=None), service_tier=None)

=== Results for groq/llama-3.1-70b-versatile ===

Model: groq/llama-3.1-70b-versatile

Summarization test:
Failed: litellm.RateLimitError: RateLimitError: GroqException - Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.1-70b-versatile` in organization `org_01hxvgcksffa282nw502agpkd9` on tokens per minute (TPM): Limit 6000, Requested 34960, please reduce your message size and try again. Visit https://console.groq.com/docs/rate-limits for more information.', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

Tool usage test:
Result: ModelResponse(id='chatcmpl-737e30ad-5ead-4f50-a8bc-40bdd24c2abd', choices=[Choices(finish_reason='stop', index=0, message=Message(content='<function=multiply({"a": 1234568789, "b": 9878654321})</function>', role='assistant', tool_calls=None, function_call=None))], created=1730579902, model='groq/llama-3.1-70b-versatile', object='chat.completion', system_fingerprint='fp_b6828be2c9', usage=Usage(completion_tokens=26, prompt_tokens=245, total_tokens=271, completion_tokens_details=None, prompt_tokens_details=None, queue_time=0.003598586000000001, prompt_time=0.041459327, completion_time=0.104, total_time=0.145459327), service_tier=None, x_groq={'id': 'req_01jbq9kbx6fvf8tbkz2g1wp5jq'})

=== Results for groq/mixtral-8x7b-32768 ===

Model: groq/mixtral-8x7b-32768

Summarization test:
Failed: litellm.RateLimitError: RateLimitError: GroqException - Error code: 413 - {'error': {'message': 'Request too large for model `mixtral-8x7b-32768` in organization `org_01hxvgcksffa282nw502agpkd9` on tokens per minute (TPM): Limit 5000, Requested 34961, please reduce your message size and try again. Visit https://console.groq.com/docs/rate-limits for more information.', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

Tool usage test:
Result: ModelResponse(id='chatcmpl-9605cdbe-62b9-4586-a95e-5b9d2a8cf62f', choices=[Choices(finish_reason='tool_calls', index=0, message=Message(content=None, role='assistant', tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"a":1234568789,"b":9878654321}', name='multiply'), id='call_539g', type='function')], function_call=None))], created=1730579903, model='groq/mixtral-8x7b-32768', object='chat.completion', system_fingerprint='fp_c5f20b5bb1', usage=Usage(completion_tokens=231, prompt_tokens=1239, total_tokens=1470, completion_tokens_details=None, prompt_tokens_details=None, queue_time=0.0013123260000000025, prompt_time=0.103170228, completion_time=0.3679172, total_time=0.471087428), service_tier=None, x_groq={'id': 'req_01jbq9kcz0em9rxsg9myd6tbq9'})

=== Results for sambanova/Meta-Llama-3.1-70B-Instruct ===

Model: sambanova/Meta-Llama-3.1-70B-Instruct

Summarization test:
Summary: The story begins with Gregor Samsa, a traveling salesman, waking up to find himself transformed into a giant vermin. He is shocked and confused, and his family is equally horrified when they discover his new form. Gregor's father, mother, and sister are forced to care for him, but they struggle to cope with the situation. As the days pass, Gregor becomes increasingly isolated and withdrawn, and his family's relationships with each other begin to deteriorate. The family's financial situation also becomes more precarious, and they are forced to take in boarders to make ends meet. Meanwhile, Gregor's sister, Grete, becomes increasingly resentful of her brother's condition and the burden it places on the family. In the end, Gregor's family decides that they can no longer care for him, and he dies alone in his room. The story ends with the family feeling a sense of relief and liberation, and they begin to make plans for a new future without Gregor.

Tool usage test:
Result: ModelResponse(id='7f812df7-7250-4288-963f-b4fab851af5f', choices=[Choices(finish_reason='stop', index=0, message=Message(content="To solve this mathematical expression, I'll break it down step by step. However, I must point out that I'm a large language model, I don't have a built-in `multiply` tool, but I can use the standard multiplication algorithm to compute the result.\n\n**Step 1: Multiply the numbers**\n\nTo multiply two large numbers, we can use the standard multiplication algorithm, which involves multiplying each digit of one number by each digit of the other number and then adding up the results.\n\nHere are the numbers:\n\n1234568789\n9878654321\n\n**Step 2: Multiply each digit**\n\nI'll multiply each digit of the first number by each digit of the second number:\n\n(1 × 9) + (1 × 8) + (1 × 7) + ... + (9 × 1) = ?\n\nThis would involve a lot of calculations, so I'll use a shortcut. I'll use the fact that the result of multiplying two numbers can be represented as a sum of partial products.\n\n**Step 3: Calculate the partial products**\n\nHere are the partial products:\n\n1 × 9878654321 = 9878654321\n2 × 9878654321 = 19757308642\n3 × 9878654321 = 29635962963\n4 × 9878654321 = 39514617284\n5 × 9878654321 = 49393271605\n6 × 9878654321 = 59271925926\n7 × 9878654321 = 69150580247\n8 × 9878654321 = 79029234568\n9 × 9878654321 = 88907888889\n\nNow, I'll add up these partial products:\n\n9878654321 + 19757308642 + 29635962963 + ... + 88907888889 = ?\n\n**Step 4: Add up the partial products**\n\nThis would involve a lot of calculations, so I'll use a calculator or a computer program to compute the result.\n\nUsing a calculator or a computer program, I get:\n\n12193263111232153789\n\nTherefore, the result of multiplying 1234568789 by 9878654321 is:\n\n12193263111232153789", role='assistant', tool_calls=None, function_call=None))], created=1730579951, model='sambanova/Meta-Llama-3.1-70B-Instruct', object='chat.completion', system_fingerprint='fastcoe', usage=Usage(completion_tokens=465, prompt_tokens=68, total_tokens=533, completion_tokens_details=None, prompt_tokens_details=None, completion_tokens_after_first_per_sec=332.57812451670264, completion_tokens_after_first_per_sec_first_ten=341.42165405293434, completion_tokens_per_sec=294.70796700710304, end_time=1730579953.3988972, is_last_response=True, start_time=1730579951.7878554, time_to_first_token=0.2158808708190918, total_latency=1.5778331502955012, total_tokens_per_sec=337.80504605330304), service_tier=None)

=== Results for sambanova/Meta-Llama-3.1-405B-Instruct ===

Model: sambanova/Meta-Llama-3.1-405B-Instruct

Summarization test:
Failed: litellm.BadRequestError: SambanovaException - The maximum context length of Meta-Llama-3.1-405B-Instruct is 8192. However, answering your request will take 31902 tokens. Please reduce the length of the messages.

Tool usage test:
Result: ModelResponse(id='b2fa07e8-6304-49a2-952c-ae278bb540ea', choices=[Choices(finish_reason='stop', index=0, message=Message(content='I am unable to complete the mathematical expression as it is too complex and the numbers are too large.', role='assistant', tool_calls=None, function_call=None))], created=1730579954, model='sambanova/Meta-Llama-3.1-405B-Instruct', object='chat.completion', system_fingerprint='fastcoe', usage=Usage(completion_tokens=20, prompt_tokens=68, total_tokens=88, completion_tokens_details=None, prompt_tokens_details=None, completion_tokens_after_first_per_sec=52.57528442733537, completion_tokens_after_first_per_sec_first_ten=65.9431992554021, completion_tokens_per_sec=30.81356536112769, end_time=1730579954.8575778, is_last_response=True, start_time=1730579954.1504178, time_to_first_token=0.34577345848083496, total_latency=0.6490647792816162, total_tokens_per_sec=135.57968758896183), service_tier=None)

=== Results for cerebras/llama3.1-70b ===

Model: cerebras/llama3.1-70b

Summarization test:
Failed: litellm.BadRequestError: CerebrasException - Error code: 400 - {'message': 'Please reduce the length of the messages or completion. Current length is 31901 while limit is 8192', 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}

Tool usage test:
Result: ModelResponse(id='chatcmpl-d5eda58d-da27-47da-beee-60bdfa89e3e1', choices=[Choices(finish_reason='tool_calls', index=0, message=Message(content=None, role='assistant', tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"a": 1234568789, "b": 9878654321}', name='multiply'), id='43986835a', type='function')], function_call=None))], created=1730579956, model='cerebras/llama3.1-70b', object='chat.completion', system_fingerprint='fp_55ebaf7e1e', usage=Usage(completion_tokens=20, prompt_tokens=267, total_tokens=287, completion_tokens_details=None, prompt_tokens_details=None), service_tier=None, time_info={'queue_time': 2.813e-05, 'prompt_time': 0.011044471052631578, 'completion_time': 0.012903178947368421, 'total_time': 0.03944087028503418, 'created': 1730579956})

=== Results for cerebras/llama3.1-8b ===

Model: cerebras/llama3.1-8b

Summarization test:
Failed: litellm.BadRequestError: CerebrasException - Error code: 400 - {'message': 'Please reduce the length of the messages or completion. Current length is 31901 while limit is 8192', 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}

Tool usage test:
Result: ModelResponse(id='chatcmpl-25ffdf0f-69ad-4d7c-b2b5-3babae9c5d0d', choices=[Choices(finish_reason='tool_calls', index=0, message=Message(content=None, role='assistant', tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"a": 1234568789, "b": 9878654321}', name='multiply'), id='da8c2d8fa', type='function')], function_call=None))], created=1730579958, model='cerebras/llama3.1-8b', object='chat.completion', system_fingerprint='fp_55ebaf7e1e', usage=Usage(completion_tokens=20, prompt_tokens=267, total_tokens=287, completion_tokens_details=None, prompt_tokens_details=None), service_tier=None, time_info={'queue_time': 2.844e-05, 'prompt_time': 0.014415873631578948, 'completion_time': 0.009098707368421052, 'total_time': 0.037596702575683594, 'created': 1730579958})

=== Results for openrouter/microsoft/phi-3-medium-128k-instruct:free ===

Model: openrouter/microsoft/phi-3-medium-128k-instruct:free

Summarization test:
Failed: litellm.BadRequestError: OpenrouterException - 

Tool usage test:
Failed: litellm.NotFoundError: NotFoundError: OpenrouterException - Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. To learn more about provider routing, visit: https://openrouter.ai/docs/provider-routing', 'code': 404}, 'user_id': 'user_2lIqNeFAVyWBRxSs5m2xfreKZNT'}

=== Results for openrouter/google/gemini-pro-1.5-exp ===

Model: openrouter/google/gemini-pro-1.5-exp

Summarization test:
Summary: "Metamorphosis" by Franz Kafka tells the story of Gregor Samsa, a traveling salesman who wakes up one morning transformed into a giant insect. His family is horrified and struggles to adapt to his new form, initially trying to care for him but eventually finding him to be a burden. Gregor's inability to communicate or provide for his family leads to his increasing isolation and neglect. As his condition deteriorates and his presence causes conflict, Gregor's family eventually wishes for him to be gone, seeing him as a monstrous creature rather than their son and brother. In the end, Gregor dies alone and neglected, and his family experiences a sense of relief and renewed hope for the future. The story explores themes of alienation, isolation, family duty, and the dehumanizing effects of modern society. 


Tool usage test:
Failed: litellm.RateLimitError: RateLimitError: OpenrouterException - 

=== Results for openrouter/google/gemini-flash-1.5-exp ===

Model: openrouter/google/gemini-flash-1.5-exp

Summarization test:
Failed: litellm.RateLimitError: RateLimitError: OpenrouterException - 

Tool usage test:
Failed: litellm.RateLimitError: RateLimitError: OpenrouterException - 

=== Results for openrouter/meta-llama/llama-3.1-405b-instruct:free ===

Model: openrouter/meta-llama/llama-3.1-405b-instruct:free

Summarization test:
Failed: litellm.BadRequestError: OpenrouterException - 

Tool usage test:
Failed: litellm.NotFoundError: NotFoundError: OpenrouterException - Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. To learn more about provider routing, visit: https://openrouter.ai/docs/provider-routing', 'code': 404}, 'user_id': 'user_2lIqNeFAVyWBRxSs5m2xfreKZNT'}

=== Results for openrouter/nousresearch/hermes-3-llama-3.1-405b:freegemini/gemini-1.5-pro-exp-0827 ===

Model: openrouter/nousresearch/hermes-3-llama-3.1-405b:freegemini/gemini-1.5-pro-exp-0827

Summarization test:
Failed: litellm.APIError: APIError: OpenrouterException - 

Tool usage test:
Failed: litellm.NotFoundError: NotFoundError: OpenrouterException - Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. To learn more about provider routing, visit: https://openrouter.ai/docs/provider-routing', 'code': 404}, 'user_id': 'user_2lIqNeFAVyWBRxSs5m2xfreKZNT'}

=== Results for gemini/gemini-1.5-flash-exp-0827 ===

Model: gemini/gemini-1.5-flash-exp-0827

Summarization test:
Failed: litellm.BadRequestError: VertexAIException BadRequestError - {
  "error": {
    "code": 400,
    "message": "User location is not supported for the API use.",
    "status": "FAILED_PRECONDITION"
  }
}


Tool usage test:
Failed: litellm.BadRequestError: VertexAIException BadRequestError - {
  "error": {
    "code": 400,
    "message": "User location is not supported for the API use.",
    "status": "FAILED_PRECONDITION"
  }
}

## LangChain based test

=== Results for groq ===

Model: llama-3.1-70b-versatile

Summarization test:
Failed: Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.1-70b-versatile` in organization `org_01hxvgcksffa282nw502agpkd9` on tokens per minute (TPM): Limit 6000, Requested 34964, please reduce your message size and try again. Visit https://console.groq.com/docs/rate-limits for more information.', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

Tool usage test:
Result: content='' additional_kwargs={'tool_calls': [{'id': 'call_xwxt', 'function': {'arguments': '{"a": 123456789, "b": 987654321}', 'name': 'multiply'}, 'type': 'function'}]} response_metadata={'token_usage': {'completion_tokens': 24, 'prompt_tokens': 244, 'total_tokens': 268, 'completion_time': 0.096, 'prompt_time': 0.045807031, 'queue_time': 0.0035783090000000017, 'total_time': 0.141807031}, 'model_name': 'llama-3.1-70b-versatile', 'system_fingerprint': 'fp_5c5d1b5cfb', 'finish_reason': 'tool_calls', 'logprobs': None} id='run-5f0a2ceb-5875-4f3e-828d-a281d7ec7cac-0' tool_calls=[{'name': 'multiply', 'args': {'a': 123456789, 'b': 987654321}, 'id': 'call_xwxt', 'type': 'tool_call'}] usage_metadata={'input_tokens': 244, 'output_tokens': 24, 'total_tokens': 268}

=== Results for sambanova ===

Model: Meta-Llama-3.1-70B-Instruct

Summarization test:
Summary: The story begins with Gregor Samsa, a traveling salesman, waking up to find himself transformed into a giant vermin. He is shocked and confused, and his family is horrified by his new appearance. Gregor's father, mother, and sister are struggling to cope with the situation, and they are unsure of how to care for him. As the days pass, Gregor becomes increasingly isolated and withdrawn, and his family's attitude towards him becomes more and more hostile. Despite his efforts to communicate with them, Gregor is unable to express himself, and he is eventually locked in his room. The family's situation becomes increasingly desperate, and they are forced to take in boarders to make ends meet. The boarders are disgusted by Gregor's presence, and they eventually give notice and leave. In the end, Gregor's family is relieved by his death, and they are able to move on with their lives. The story explores themes of identity, isolation, and the breakdown of family relationships.

Tool usage test:
Failed: 

Model: Meta-Llama-3.1-405B-Instruct

Summarization test:
Failed: ('Sambanova /complete call failed with status code 400.', 'The maximum context length of Meta-Llama-3.1-405B-Instruct is 8192. However, answering your request will take 32929 tokens. Please reduce the length of the messages or the specified max_completion_tokens value.\n.')

Tool usage test:
Failed: 

=== Results for cerebras ===

Model: llama3.1-70b

Summarization test:
Failed: Error code: 400 - {'message': 'Please reduce the length of the messages or completion. Current length is 31905 while limit is 8192', 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}

Tool usage test:
Result: content='' additional_kwargs={'tool_calls': [{'id': 'c9b9bce84', 'function': {'arguments': '{"a": 123456789, "b": 987654321}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 263, 'total_tokens': 281, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'llama3.1-70b', 'system_fingerprint': 'fp_55ebaf7e1e', 'finish_reason': 'tool_calls', 'logprobs': None} id='run-f01a720f-e9f1-4402-8dea-470d25b34e97-0' tool_calls=[{'name': 'multiply', 'args': {'a': 123456789, 'b': 987654321}, 'id': 'c9b9bce84', 'type': 'tool_call'}] usage_metadata={'input_tokens': 263, 'output_tokens': 18, 'total_tokens': 281, 'input_token_details': {}, 'output_token_details': {}}

Model: llama3.1-8b

Summarization test:
Failed: Error code: 400 - {'message': 'Please reduce the length of the messages or completion. Current length is 31905 while limit is 8192', 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}

Tool usage test:
Result: content='' additional_kwargs={'tool_calls': [{'id': '01d54e23e', 'function': {'arguments': '{"a": 123456789, "b": 987654321}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 263, 'total_tokens': 281, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'llama3.1-8b', 'system_fingerprint': 'fp_55ebaf7e1e', 'finish_reason': 'tool_calls', 'logprobs': None} id='run-3a5caeb2-fe6e-4741-ae51-ec38d213096f-0' tool_calls=[{'name': 'multiply', 'args': {'a': 123456789, 'b': 987654321}, 'id': '01d54e23e', 'type': 'tool_call'}] usage_metadata={'input_tokens': 263, 'output_tokens': 18, 'total_tokens': 281, 'input_token_details': {}, 'output_token_details': {}}

=== Results for openrouter ===

Model: microsoft/phi-3-medium-128k-instruct:free

Summarization test:
Summary:  "Metamorphosis" is an ebook by Franz Kafka, available for free. The Project Gutenberg ebooks are made available at no charge and under certain conditions. The Project Gutenberg copyrights statement. Further information on donations is available on the Project Gutenberg website.

The Project Gutenberg is a non-profit organization, but we have no one. The Project Gutenberg is not available at no charge. The Project Gutenberg is a 501(c) donations to The Project Gutenberg is not available at no charge. Supporting The Project Gutenberg through the Internet.

Title: "Metamorphosis

Author: Franz Kafka

Translator: David Wyllie

Release date: August 17, 2005, 2005, 201.

Language: English

The Project Gutenberg is a 501.

Metamorphosis is a 501.


I

Gregor Samsa wakes up to realize that he has been transformed into a horrible vermin. Gregor is the original language of this text.

Translator: David Wyllie

Release date: August 17, 2005, 201.

More information about donations are available on the Project Gutenberg website.

Section 4.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

** This is a copyrighted Project Gutenberg eBook. Details below.

**

This is a copyrighted Project Gutenberg ebook.

The Project Gutenberg is a 501.

The Project Gutenberg is not available at no charge.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

For more information about donations, please visit the Project Gutenberg website.

Public domain works are available at no charge.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.
The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

The Project Gutenberg is a 501.

Tool usage test:
Failed: Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. To learn more about provider routing, visit: https://openrouter.ai/docs/provider-routing', 'code': 404}, 'user_id': 'user_2lIqNeFAVyWBRxSs5m2xfreKZNT'}

Model: google/gemini-pro-1.5-exp

Summarization test:
Summary: "Metamorphosis" by Franz Kafka tells the story of Gregor Samsa, a traveling salesman who awakens one morning transformed into a giant insect. His shocking metamorphosis causes his family great distress and forces them to confront their dependence on him and their own revulsion at his new form. As Gregor's ability to communicate and care for himself diminishes, his family struggles to adapt, eventually reaching a point of despair and resentment. The story ends with Gregor's death, after which his family experiences a sense of relief and newfound hope for the future. The novella explores themes of alienation, duty, family dynamics, and the dehumanizing effects of modern society.  This particular edition is part of Project Gutenberg, which offers free access to ebooks in the public domain.

Tool usage test:
Failed: {'message': '{\n  "error": {\n    "code": 429,\n    "message": "Quota exceeded for quota metric \'Generate Content API requests per minute\' and limit \'GenerateContent request limit per minute for a region\' of service \'generativelanguage.googleapis.com\' for consumer \'project_number:712835604272\'.",\n    "status": "RESOURCE_EXHAUSTED",\n    "details": [\n      {\n        "@type": "type.googleapis.com/google.rpc.ErrorInfo",\n        "reason": "RATE_LIMIT_EXCEEDED",\n        "domain": "googleapis.com",\n        "metadata": {\n          "consumer": "projects/712835604272",\n          "quota_limit_value": "1500",\n          "quota_location": "us-east7",\n          "service": "generativelanguage.googleapis.com",\n          "quota_limit": "GenerateContentRequestsPerMinutePerProjectPerRegion",\n          "quota_metric": "generativelanguage.googleapis.com/generate_content_requests"\n        }\n      },\n      {\n        "@type": "type.googleapis.com/google.rpc.Help",\n        "links": [\n          {\n            "description": "Request a higher quota limit.",\n            "url": "https://cloud.google.com/docs/quotas/help/request_increase"\n          }\n        ]\n      }\n    ]\n  }\n}\n', 'code': 429}

Model: google/gemini-flash-1.5-exp

Summarization test:
Failed: {'message': '{\n  "error": {\n    "code": 429,\n    "message": "Quota exceeded for quota metric \'Generate Content API requests per minute\' and limit \'GenerateContent request limit per minute for a region\' of service \'generativelanguage.googleapis.com\' for consumer \'project_number:712835604272\'.",\n    "status": "RESOURCE_EXHAUSTED",\n    "details": [\n      {\n        "@type": "type.googleapis.com/google.rpc.ErrorInfo",\n        "reason": "RATE_LIMIT_EXCEEDED",\n        "domain": "googleapis.com",\n        "metadata": {\n          "quota_metric": "generativelanguage.googleapis.com/generate_content_requests",\n          "quota_limit": "GenerateContentRequestsPerMinutePerProjectPerRegion",\n          "quota_location": "us-east7",\n          "quota_limit_value": "1500",\n          "service": "generativelanguage.googleapis.com",\n          "consumer": "projects/712835604272"\n        }\n      },\n      {\n        "@type": "type.googleapis.com/google.rpc.Help",\n        "links": [\n          {\n            "description": "Request a higher quota limit.",\n            "url": "https://cloud.google.com/docs/quotas/help/request_increase"\n          }\n        ]\n      }\n    ]\n  }\n}\n', 'code': 429}

Tool usage test:
Failed: {'message': '{\n  "error": {\n    "code": 429,\n    "message": "Resource has been exhausted (e.g. check quota).",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n', 'code': 429}

Model: meta-llama/llama-3.1-405b-instruct:freenousresearch/hermes-3-llama-3.1-405b:free

Summarization test:
Failed: {'message': 'This endpoint\'s maximum context length is 32768 tokens. However, you requested about 36397 tokens (36397 of text input). Please reduce the length of either one, or use the "middle-out" transform to compress your prompt automatically.', 'code': 400}

Tool usage test:
Failed: Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. To learn more about provider routing, visit: https://openrouter.ai/docs/provider-routing', 'code': 404}, 'user_id': 'user_2lIqNeFAVyWBRxSs5m2xfreKZNT'}

=== Results for google ===

Model: gemini-1.5-pro-exp-0827

Summarization test:
Failed: Your location is not supported by google-generativeai at the moment. Try to use ChatVertexAI LLM from langchain_google_vertexai.

Tool usage test:
Failed: Your location is not supported by google-generativeai at the moment. Try to use ChatVertexAI LLM from langchain_google_vertexai.

Model: gemini-1.5-flash-exp-0827

Summarization test:
Failed: Your location is not supported by google-generativeai at the moment. Try to use ChatVertexAI LLM from langchain_google_vertexai.

Tool usage test:
Failed: Your location is not supported by google-generativeai at the moment. Try to use ChatVertexAI LLM from langchain_google_vertexai.

=== Results for github ===

Model: gpt-4o

Summarization test:
Failed: Error code: 413 - {'error': {'code': 'tokens_limit_reached', 'message': 'Request body too large for gpt-4o model. Max size: 8000 tokens.', 'details': 'Request body too large for gpt-4o model. Max size: 8000 tokens.'}}

Tool usage test:
Result: content="To solve the mathematical expression \\( 123456789 \\times 987654321 \\), we will use the calculator tool to compute the result. Here's how we can approach solving the expression:\n\n1. Identify the numbers to be multiplied: \\( a = 123456789 \\) and \\( b = 987654321 \\).\n2. Use the calculator tool to compute the product.\n\nLet's proceed with the calculation using the tool." additional_kwargs={'tool_calls': [{'id': 'call_95Gx3GPzL5S2cYacpyPLsYZb', 'function': {'arguments': '{"a":123456789,"b":987654321}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 108, 'prompt_tokens': 75, 'total_tokens': 183, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_d54531d9eb', 'finish_reason': 'tool_calls', 'logprobs': None} id='run-c4c37542-af3d-4f50-9866-434019342c84-0' tool_calls=[{'name': 'multiply', 'args': {'a': 123456789, 'b': 987654321}, 'id': 'call_95Gx3GPzL5S2cYacpyPLsYZb', 'type': 'tool_call'}] usage_metadata={'input_tokens': 75, 'output_tokens': 108, 'total_tokens': 183, 'input_token_details': {}, 'output_token_details': {}}

Model: gpt-4o-mini

Summarization test:
Failed: Error code: 413 - {'error': {'code': 'tokens_limit_reached', 'message': 'Request body too large for gpt-4o-mini model. Max size: 8000 tokens.', 'details': 'Request body too large for gpt-4o-mini model. Max size: 8000 tokens.'}}

Tool usage test:
Result: content='' additional_kwargs={'tool_calls': [{'id': 'call_2yKVqhOCy2zXWQh5G0N2J6vd', 'function': {'arguments': '{"a":123456789,"b":987654321}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 75, 'total_tokens': 96, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': 'fp_d54531d9eb', 'finish_reason': 'tool_calls', 'logprobs': None} id='run-535b3f71-2b1f-4596-b3fb-c1f7dc659e8d-0' tool_calls=[{'name': 'multiply', 'args': {'a': 123456789, 'b': 987654321}, 'id': 'call_2yKVqhOCy2zXWQh5G0N2J6vd', 'type': 'tool_call'}] usage_metadata={'input_tokens': 75, 'output_tokens': 21, 'total_tokens': 96, 'input_token_details': {}, 'output_token_details': {}}

Model: Meta-Llama-3.1-405B-Instruct

Summarization test:
Failed: Error code: 413 - {'error': {'code': 'tokens_limit_reached', 'message': 'Request body too large for meta-llama-3.1-405b-instruct model. Max size: 8000 tokens.', 'details': 'Request body too large for meta-llama-3.1-405b-instruct model. Max size: 8000 tokens.'}}

Tool usage test:
Result: content='{"name": "multiply", "parameters": {"a": "123456789", "b": "987654321"}}<|eom_id|>' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 27, 'prompt_tokens': 218, 'total_tokens': 245, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'Meta-Llama-3-405B-Instruct', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-6c4560a4-cb2a-4f74-9933-54497787a0e6-0' usage_metadata={'input_tokens': 218, 'output_tokens': 27, 'total_tokens': 245, 'input_token_details': {}, 'output_token_details': {}}
