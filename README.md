# free-models-checking
Smoke-test for free models


=== Results for groq ===

Model: llama-3.1-70b-versatile

Summarization test:
Failed: Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.1-70b-versatile` in organization `org_01hxvgcksffa282nw502agpkd9` on tokens per minute (TPM): Limit 6000, Requested 34964, please reduce your message size and try again. Visit https://console.groq.com/docs/rate-limits for more information.', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}

Tool usage test:
Result: content='' additional_kwargs={'tool_calls': [{'id': 'call_2fft', 'function': {'arguments': '{"a": "123456789", "b": "987654321"}', 'name': 'multiply'}, 'type': 'function'}]} response_metadata={'token_usage': {'completion_tokens': 25, 'prompt_tokens': 244, 'total_tokens': 269, 'completion_time': 0.1, 'prompt_time': 0.047873172, 'queue_time': 0.0034489340000000007, 'total_time': 0.147873172}, 'model_name': 'llama-3.1-70b-versatile', 'system_fingerprint': 'fp_9260b4bb2e', 'finish_reason': 'tool_calls', 'logprobs': None} id='run-119f4907-64c5-40f3-8799-b2ab5e119611-0' tool_calls=[{'name': 'multiply', 'args': {'a': '123456789', 'b': '987654321'}, 'id': 'call_2fft', 'type': 'tool_call'}] usage_metadata={'input_tokens': 244, 'output_tokens': 25, 'total_tokens': 269}

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
Result: content='' additional_kwargs={'tool_calls': [{'id': 'd59c4cef2', 'function': {'arguments': '{"a": 123456789, "b": 987654321}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 263, 'total_tokens': 281, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'llama3.1-70b', 'system_fingerprint': 'fp_55ebaf7e1e', 'finish_reason': 'tool_calls', 'logprobs': None} id='run-1fbaa001-0baa-4e77-82dd-24e9bc9778d9-0' tool_calls=[{'name': 'multiply', 'args': {'a': 123456789, 'b': 987654321}, 'id': 'd59c4cef2', 'type': 'tool_call'}] usage_metadata={'input_tokens': 263, 'output_tokens': 18, 'total_tokens': 281, 'input_token_details': {}, 'output_token_details': {}}

Model: llama3.1-8b

Summarization test:
Failed: Error code: 400 - {'message': 'Please reduce the length of the messages or completion. Current length is 31905 while limit is 8192', 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}

Tool usage test:
Result: content="To solve this problem, we'll multiply the two numbers step by step. \n\nFirst, let's break down the numbers into more manageable parts:\n\n123456789 = 100,000,000 + 20,000,000 + 3,000,000 + 400,000 + 50,000 + 6,000 + 700 + 80 + 9\n\n987654321 = 900,000,000 + 80,000,000 + 7,000,000 + 600,000 + 20,000 + 3,000 + 400 + 80 + 1\n\nNow, let's multiply the numbers:\n\n(100,000,000 * 900,000,000) + (100,000,000 * 80,000,000) + (100,000,000 * 7,000,000) + (100,000,000 * 600,000) + (100,000,000 * 20,000) + (100,000,000 * 3,000) + (100,000,000 * 400) + (100,000,000 * 80) + (100,000,000 * 9) + (20,000,000 * 80,000,000) + (20,000,000 * 7,000,000) + (20,000,000 * 600,000) + (20,000,000 * 20,000) + (20,000,000 * 3,000) + (20,000,000 * 400) + (20,000,000 * 80) + (20,000,000 * 9) + (3,000,000 * 600,000) + (3,000,000 * 20,000) + (3,000,000 * 3,000) + (3,000,000 * 400) + (3,000,000 * 80) + (3,000,000 * 9) + (400,000 * 20,000) + (400,000 * 3,000) + (400,000 * 400) + (400,000 * 80) + (400,000 * 9) + (50,000 * 20,000) + (50,000 * 3,000) + (50,000 * 400) + (50,000 * 80) + (50,000 * 9) + (6,000 * 20,000) + (6,000 * 3,000) + (6,000 * 400) + (6,000 * 80) + (6,000 * 9) + (700 * 20,000) + (700 * 3,000) + (700 * 400) + (700 * 80) + (700 * 9) + (80 * 20,000) + (80 * 3,000) + (80 * 400) + (80 * 9) + (9 * 20,000) + (9 * 3,000) + (9 * 400) + (9 * 80) + (9 * 9)\n\nNow, let's perform the multiplications:\n\n(90,000,000,000,000) + (8,000,000,000,000) + (700,000,000,000) + (60,000,000,000) + (2,000,000,000) + (300,000,000) + (40,000,000) + (8,000,000) + (900,000,000) + (1,600,000,000,000) + (140,000,000,000) + (1,400,000,000) + (120,000,000) + (60,000,000) + (120,000,000) + (8,000,000) + (1,600,000,000) + (180,000,000) + (180,000,000) + (3,600,000) + (1,200,000) + (400,000) + (80,000) + (36,000,000) + (1,200,000) + (400,000) + (80,000) + (4,200,000) + (2,100,000) + (280,000) + (28,000) + (2,520,000) + (28,000) + (400,000) + (80,000) + (4,200,000) + (28,000)\n\nNow, let's add up the results:\n\n121,445,767,000,000,000\n\nThis is the result of the multiplication of 123456789 and 987654321." additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 1034, 'prompt_tokens': 263, 'total_tokens': 1297, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'llama3.1-8b', 'system_fingerprint': 'fp_55ebaf7e1e', 'finish_reason': 'stop', 'logprobs': None} id='run-26812b17-0374-4f1e-a350-dbcc0ac1e66e-0' usage_metadata={'input_tokens': 263, 'output_tokens': 1034, 'total_tokens': 1297, 'input_token_details': {}, 'output_token_details': {}}

=== Results for openrouter ===

Model: microsoft/phi-3-medium-128k-instruct:free

Summarization test:
Summary:  "Metamorphosis" is a free eBooks must be available to anyone in the United States and most other parts of the world. These materials are provided in compliance with the Project Gutenberg eBooks are free to anyone in the United States and most other parts of the world at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg eBooks are available at no cost. If you are not located in the United States, you will have to check the laws of the country where you are located before using this eBooks.

This eBooks are copyrighted by the Project Gutenberg and are distributed under the terms of the Project Gutenberg.

This eBooks are copyrighted by the Project Gutenberg and are distributed under the terms of the Project Gutenberg.

"Metamorphosis" is a free eBooks must be available to anyone in the United States and most other parts of the world at no cost and with almost no restrictions whatsoever.

This eBooks are copyrighted by the Project Gutenberg and are distributed under the terms of the Project Gutenberg.

"Metamorphosis", translated by David Wyllie, released on August 17, 2005, 2005, 2005, 2005, 2005, 205, 2005, 2005, 2005, 205, 2005, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 2

Tool usage test:
Failed: Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. To learn more about provider routing, visit: https://openrouter.ai/docs/provider-routing', 'code': 404}, 'user_id': 'user_2lIqNeFAVyWBRxSs5m2xfreKZNT'}

Model: google/gemini-pro-1.5-exp

Summarization test:
Failed: {'message': '{\n  "error": {\n    "code": 429,\n    "message": "Resource has been exhausted (e.g. check quota).",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n', 'code': 429}

Tool usage test:
Failed: {'message': '{\n  "error": {\n    "code": 429,\n    "message": "Resource has been exhausted (e.g. check quota).",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n', 'code': 429}

Model: google/gemini-flash-1.5-exp

Summarization test:
Failed: {'message': '{\n  "error": {\n    "code": 429,\n    "message": "Quota exceeded for quota metric \'Generate Content API requests per minute\' and limit \'GenerateContent request limit per minute for a region\' of service \'generativelanguage.googleapis.com\' for consumer \'project_number:712835604272\'.",\n    "status": "RESOURCE_EXHAUSTED",\n    "details": [\n      {\n        "@type": "type.googleapis.com/google.rpc.ErrorInfo",\n        "reason": "RATE_LIMIT_EXCEEDED",\n        "domain": "googleapis.com",\n        "metadata": {\n          "quota_limit": "GenerateContentRequestsPerMinutePerProjectPerRegion",\n          "quota_limit_value": "1500",\n          "quota_metric": "generativelanguage.googleapis.com/generate_content_requests",\n          "consumer": "projects/712835604272",\n          "quota_location": "us-east7",\n          "service": "generativelanguage.googleapis.com"\n        }\n      },\n      {\n        "@type": "type.googleapis.com/google.rpc.Help",\n        "links": [\n          {\n            "description": "Request a higher quota limit.",\n            "url": "https://cloud.google.com/docs/quotas/help/request_increase"\n          }\n        ]\n      }\n    ]\n  }\n}\n', 'code': 429}

Tool usage test:
Failed: {'message': '{\n  "error": {\n    "code": 429,\n    "message": "Resource has been exhausted (e.g. check quota).",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n', 'code': 429}

Model: meta-llama/llama-3.1-405b-instruct:free

Summarization test:
Failed: {'message': '{"error":{"code":null,"message":"Rate limit exceeded","param":null,"type":"rate_limit_exceeded"}}\n', 'code': 429}

Tool usage test:
Failed: Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. To learn more about provider routing, visit: https://openrouter.ai/docs/provider-routing', 'code': 404}, 'user_id': 'user_2lIqNeFAVyWBRxSs5m2xfreKZNT'}