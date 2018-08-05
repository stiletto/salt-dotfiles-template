all: apply

apply:
	bash ./salt-call state.apply

.PHONY: apply
