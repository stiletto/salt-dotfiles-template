all: apply

apply:
	bash ./salt-call state.apply

sync_grains:
	bash ./salt-call saltutil.sync_grains -l debug

.PHONY: apply sync_grains
