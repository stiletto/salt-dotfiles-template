# How to use:

1. Fork this repo
1. Put your states and `top.sls` in this directory, put your pillar in `_pillar`.
1. Run `./salt-call state.apply`
1. Probably add a function similar to this to your `~/.*shrc`:

```
dotfiles-apply() {
  {{ opts['file_roots']['base'][0] }}/salt-call state.apply "$@"
}
```
