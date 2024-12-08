


### **2. Create a Table with Merged Cells**

**Question:**  
Create a table that has a header row spanning 3 columns and a footer spanning 2 rows.

**Solution:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table with Merged Cells</title>
</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <th colspan="3">Header Row</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Row 1 Col 1</td>
                <td>Row 1 Col 2</td>
                <td>Row 1 Col 3</td>
            </tr>
            <tr>
                <td>Row 2 Col 1</td>
                <td colspan="2" rowspan="2">Footer spanning 2 rows</td>
            </tr>
            <tr>
                <td>Row 3 Col 1</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```


to check :

{

understand rowspan and colspan clearly.. 
}

