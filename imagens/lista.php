<?php

    /*var_dump($_REQUEST);
    var_dump($_FILES);

    $caminho = $_FILES['arquivo']['tmp_name'];
    $conteudo = file_get_contents($caminho);
    $codificado = base64_encode($conteudo);
    $descricao = $_REQUEST['descricao'];*/
$conexao = new pdo('sqlite:banco');
$sql = "select * from imagem;";
$resultado = $conexao->query($sql)->fetchAll(2);
    unset($conexao);
    foreach($resultado as $imagem){
        print'<img src="data:image/jpeg;base64,'.$imagem['conteudo'].'"/>';
        

    }

?>