import traceback
from typing import AsyncIterable, Iterable

import aiohttp
import requests
from betterproto import Casing

from maitai._config import config
from maitai._maitai_client import MaitaiClient
from maitai._types import AsyncChunkQueue, ChunkQueue, EvaluateCallback, QueueIterable
from maitai_gen.chat import ChatCompletionParams, ChatCompletionRequest
from maitai_gen.inference import InferenceStreamResponse


class Inference(MaitaiClient):

    def __init__(self):
        super().__init__()

    @classmethod
    def infer(cls, session_id, reference_id, action_type, application_ref_name, completion_params: ChatCompletionParams, apply_corrections: bool, evaluation_enabled: bool, evaluate_callback: EvaluateCallback = None,
              timeout=None) -> Iterable[InferenceStreamResponse]:
        chat_request: ChatCompletionRequest = cls.create_inference_request(application_ref_name, session_id, reference_id, action_type, apply_corrections, evaluation_enabled, completion_params)
        if evaluate_callback:
            q = ChunkQueue()
            cls.run_async(cls.send_inference_request_async(chat_request, chunk_queue=q, evaluation_callback=evaluate_callback))
            return QueueIterable(q, timeout=timeout)
        else:
            return cls.send_inference_request(chat_request)

    @classmethod
    async def infer_async(cls, session_id, reference_id, action_type, application_ref_name, completion_params: ChatCompletionParams, apply_corrections: bool, evaluation_enabled: bool,
                          evaluate_callback: EvaluateCallback = None,
                          timeout=None) -> AsyncIterable[InferenceStreamResponse]:
        chat_request: ChatCompletionRequest = cls.create_inference_request(application_ref_name, session_id, reference_id, action_type, apply_corrections, evaluation_enabled, completion_params)
        q = AsyncChunkQueue()
        cls.run_async(cls.send_inference_request_async(chat_request, async_chunk_queue=q, evaluation_callback=evaluate_callback))
        return QueueIterable(q, timeout=timeout)

    @classmethod
    def create_inference_request(cls, application_ref_name, session_id, reference_id, action_type, apply_corrections, evaluation_enabled, completion_params: ChatCompletionParams):
        infer_request: ChatCompletionRequest = ChatCompletionRequest()
        infer_request.application_ref_name = application_ref_name
        infer_request.reference_id = reference_id
        infer_request.session_id = session_id
        infer_request.action_type = action_type
        infer_request.apply_corrections = apply_corrections
        infer_request.params = completion_params
        infer_request.evaluation_enabled = evaluation_enabled
        return infer_request

    @classmethod
    def send_inference_request(cls, chat_request: ChatCompletionRequest) -> Iterable[InferenceStreamResponse]:
        def consume_stream():
            host = config.maitai_host
            url = f'{host}/chat/completions/serialized'
            headers = {
                'Content-Type': 'application/json',
                'x-api-key': config.api_key
            }
            response = requests.post(url, headers=headers, data=chat_request.to_json(casing=Casing.SNAKE), verify=False, stream=True)
            if response.status_code != 200:
                print(f"Failed to send inference request. Status code: {response.status_code}. Error: {response.text}")
                return
            else:
                print(f"Successfully sent inference request. Status code: {response.status_code}")
            try:
                for line in response.iter_lines():
                    if line:
                        yield line
            finally:
                response.close()

        for resp in consume_stream():
            inference_response: InferenceStreamResponse = InferenceStreamResponse().from_json(resp)
            yield inference_response

    @classmethod
    async def send_inference_request_async(cls, chat_request: ChatCompletionRequest, chunk_queue: ChunkQueue = None, async_chunk_queue: AsyncChunkQueue = None, evaluation_callback: EvaluateCallback = None):
        host = config.maitai_host
        url = f'{host}/chat/completions/serialized'
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': config.api_key
        }
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post(url, headers=headers, data=chat_request.to_json(casing=Casing.SNAKE)) as response:
                if response.status != 200:
                    error_text = await response.text()
                    print(f"Failed to send evaluation request. Status code: {response.status}. Error: {error_text}")
                    if chunk_queue:
                        chunk_queue.put("done")
                    if async_chunk_queue:
                        await async_chunk_queue.put("done")
                    return
                async for line in response.content:
                    if line:
                        inference_response: InferenceStreamResponse = InferenceStreamResponse().from_json(line)
                        if chunk_queue:
                            chunk_queue.put(inference_response)
                        if async_chunk_queue:
                            await async_chunk_queue.put(inference_response)
                        if inference_response.evaluate_response and evaluation_callback:
                            try:
                                evaluation_callback(inference_response.evaluate_response)
                            except:
                                traceback.print_exc()
                if chunk_queue:
                    chunk_queue.put("done")
                if async_chunk_queue:
                    await async_chunk_queue.put("done")
