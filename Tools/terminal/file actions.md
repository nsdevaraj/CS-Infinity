
```bash
find . -name "node_modules" -type d -prune -exec rm -rf '{}' +
```

this will delete folder named "node_modules" recursively 



```bash
du -sh node_modules/* | sort -hr | head -n 20
```


That’ll show you the 20 biggest folders inside `node_modules`.

