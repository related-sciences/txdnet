# TxDNet

There are many established mechanisms through which a drug target influences a disease.  Some of the best known examples come from 1) mechanisms of action for approved drugs and 2) genetic etiologies inferred from rare disease patients.  The intent of this project is to provide a structured, public data resource that models highly validated mechanisms like this, while leveraging state of the art generative AI to ensure that these mechanisms are both detailed and maintainable.

The primary use case for this resource will be to evaluate largely or fully automated, high-throughput methods that infer mechanistic links between drug targets and disease at a scale beyond curated resources (like this one).  Some questions and/or use cases this resource will be helpful for are:

- I have built a large knowledge graph based on many structured data resources and used it to predict novel links between targets and diseases, as well as propose why those links exist – how can I evaluate these predictions beyond the existence of the link itself?  In other words, is the therapeutic hypothesis implied by the prediction valid?
- I have inferred mechanistic links between targets and diseases algorithmically over a body of literature expanding well beyond highly curated, aggregated sources like Orphanet, UpToDate, OMIM, GARD, etc. – how can I assess both the prioritization of the target + disease pairs and the plausibility of the link between them?
- I have used high-throughput imaging, omics or other phenotyping data to propose new target → disease links – how can I validate that this method can recover established links well first?
- What drugs for common diseases were repurposed for rare disease, and in what ways does the mechanism of action differ for those indications (if any)?
- How can I work with a semi-structured representation of disease mechanisms that is not necessarily constrained by ontologies, entity grounding/linking, or other nomenclatures that inevitably force a loss of potentially important context?

## Development

- Install `mamba` (see https://mamba.readthedocs.io/en/latest/installation.html)
- Create environment: `mamba env create -f environment.yaml`
- Install pre-commit hooks: `pre-commit install`
- Create a `.env` file with at least these variables:

```bash
OPENAI_API_KEY="xxxxx"
PYTHONPATH=/path/to/repo 
```
