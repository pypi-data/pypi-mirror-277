[![Documentation Status](https://readthedocs.com/projects/ai-weave-weave/badge/?version=latest&token=cf7871cbb6f655983ebdb1c55c64ce6aca444984cf76225cb781139b0cee0856)](https://ai-weave-weave.readthedocs-hosted.com/en/latest/?badge=latest)

# Weave - Private Preview

**Weave is in private preview ONLY to a select few people by invitation only; for the purposes of private feedback**

**The framework for building agents - from dev to prod.**

## NOTICE

Weave is scheduled for releas in the coming week. This repo is undergoing a final rector including:

* Redoing the packaging for pypi packaging
* Integration with readthedocs.org
* Examples & Tutorials are being re-worked
* Readmes are being re-worked
* Some repo / package structure is being improved


Thank you for checking this out in the private preview. 

## Getting Started

**See the getting started tutorials: [Tutorials](examples/tutorials/README.md)**

Install the preview package:

```
pip install -r requirements.txt
python setup.py develop
```

Export at least one API key shown below. More API keys will give you access to more models.

```
export TOGETHER_API_KEY=...
export ANTHROPIC_API_KEY=sk-...
export OPENAI_API_KEY=sk-...
```

And start building your agent:

```python
import weave

answer = weave.Weave('What has keys but cannot open locks?').infer()
answer.print()
```

There is a lot of help available:

* View some basic [Getting Started](examples/tutorials/getting_started.ipynb)
* Configuring and Choosing models [Config and Models](examples/tutorials/configure.ipynb)
* Understanding the graph backend execution [Graph Execution](examples/tutorials/graphs.ipynb)


## Why weave is winning

Weave stands out on 3 key points:


1. Production Grade - predicable execution which is customizable, logged and measured.
2. Developer Friendly - beuatiful code with simple APIs, helpful error messages, and extensible.
3. Community Oriented - built better because it's built together.


Weave is the simplest, easiest, and most powerful.

* A simple, intuitive way to generate text, JSON, and images
* A suite of evaluation tools for both prompts and models
* Organize your agents, prompts, and templates
* Export and share your agents
* Rich debugging, logging, and helpful errors
* You keep ultimate control over each token
