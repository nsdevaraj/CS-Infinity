
Here’s a **crisp table** of Vim motions:




### **1. Basic Motions**

|Motion|Action|
|---|---|
|`h`|Left|
|`l`|Right|
|`j`|Down|
|`k`|Up|
|`w`|Next word|
|`b`|Previous word|
|`e`|End of word|
|`ge`|End of previous word|

### **2. Line Motions**

|Motion|Action|
|---|---|
|`0`|Beginning of line|
|`^`|First non-blank char|
|`$`|End of line|

### **3. Paragraph & Sentence**

|Motion|Action|
|---|---|
|`{`|Start of paragraph|
|`}`|End of paragraph|
|`(`|Start of sentence|
|`)`|End of sentence|

### **4. Screen Motions**

|Motion|Action|
|---|---|
|`H`|Top of screen|
|`M`|Middle of screen|
|`L`|Bottom of screen|
|`Ctrl-d`|Half-page down|
|`Ctrl-u`|Half-page up|
|`Ctrl-f`|Full-page down|
|`Ctrl-b`|Full-page up|

### **5. Search & Jump**

|Motion|Action|
|---|---|
|`/pattern`|Search forward|
|`?pattern`|Search backward|
|`n`|Next occurrence|
|`N`|Previous occurrence|
|`gg`|Beginning of file|
|`G`|End of file|
|`''`|Jump to last cursor position|

### **6. Text Object Motions**

|Motion|Action|
|---|---|
|`aw`|A word|
|`iw`|Inner word|
|`ap`|A paragraph|
|`ip`|Inner paragraph|
|`a"`|A quoted string|
|`i"`|Inner quoted string|
|`a(` / `ab`|A block (parentheses)|
|`i(` / `ib`|Inner block|

### **7. Combo Examples**

|Motion|Action|
|---|---|
|`daw`|Delete a word|
|`ci"`|Change inside quotes|
|`yap`|Yank (copy) a paragraph|
