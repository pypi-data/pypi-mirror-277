.PHONY: samples

samples:
	@echo "Generating samples..."
	for spec in samples/spec-*; do \
			PYTHONPATH=../../.. python -m app.reports.portfolio.make --spec $$spec --org spyderdemo --api_key $$PROD_API_KEY --api_url https://api.spyderbat.com --output samples/sample;  \
		done

