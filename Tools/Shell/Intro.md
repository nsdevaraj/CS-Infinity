

Shell programming focuses on writing and executing commands in a Unix shell, with an emphasis on **Bash (Bourne Again Shell)**. Other shells like `sh`, `csh`, and `tcsh` may have slight variations but follow similar principles.

### Executing Shell Commands

Commands can be run:

1. **Directly at the shell prompt.**
2. **Using a shell script**—a text file containing commands in execution order.

To run a script:

- Ensure execution permission:
    
    ```bash
    chmod +x filename.sh
    ```
    
- Execute:
    
    ```bash
    ./filename.sh
    ```
    

### The Shebang (`#!`)

The first line of a shell script defines the interpreter:

```bash
#!/bin/bash
```

Ensure the correct path using:

```bash
which bash
```

If the path is incorrect, execution may fail with **"Command not found."**

### Adding Comments

Use `#` to add comments:

```bash
# This is a comment  
echo "Hello, World!"  # This prints text  
```

### Identifying the Active Shell

Find your active shell type:

```bash
ps | grep $$
```

Example output:

```
987 tty1 00:00:00 bash
```

Check the shell interpreter’s full path:

```bash
which bash
```

Example output:

```
/bin/bash
```

This ensures your script’s shebang line (`#!`) matches the correct shell path.


### enter and exist bash interactive terminal

```bash
bash #for enter
exit # for exit
```


