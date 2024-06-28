<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1> upload e armazenamento de arquivvos </h1>
    <form method="post" action="processo.php" enctype="multipart/form-data">
    <input type="text" name="descricao" placeholder="descreva o arquivo"/>
    <input type="file" name="arquivo"/>
    <input type="submit" name="subir"/>
    </form>
</body>
</html>