---
name: inference-performance
description: Analyze model inference latency, throughput, memory, batching, concurrency, kernels, quantization, and serving bottlenecks from measurements.
category: performance
---

# Inference Performance Analysis

## Variables

- Serving target: {{target}}
- Current profile/metrics: {{profile}}
- Hardware and runtime: {{environment}}
- Quality and cost constraints: {{constraints}}

## Prompt

Use {{profile}} to locate the dominant inference bottleneck for {{target}}.

Normalize measurements by model revision, input/output length, batch size, concurrency, warm-up, precision and hardware. Separate:

- preprocessing and tokenization;
- queueing and scheduling;
- prefill and decode;
- model compute and kernels;
- memory transfer and KV cache;
- postprocessing and network;
- cold start and compilation.

Report p50, p95 and p99 latency where available, throughput, utilization, peak memory and cost per useful unit. Identify whether the workload is compute-bound, memory-bound, I/O-bound or queue-bound.

Return ranked bottlenecks, supporting evidence, the smallest discriminating benchmark, optimization candidates, expected trade-offs and a validation matrix.

Do not recommend quantization, batching or speculative decoding without stating the expected quality, latency and memory effect. Do not compare measurements from incompatible workloads.
