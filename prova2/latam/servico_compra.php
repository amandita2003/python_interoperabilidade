<?php
    $txt = file_get_contents('php://input');
    $obj = json_decode($txt,true);
    $cpf = $obj['cpf'];
    $nome = $obj['nome'];
    $id = $obj['id'];
    
    $select = "select  id  
    from cliente 
    where cpf =  '".$cpf."' ;";

	$conexao = new pdo ('sqlite:database');
	 
  $resultado = $conexao->query($select)->fetchAll(2);

  if ($resultado[0]['id'] > 0) {
    $idCliente = $resultado[0]['id'];
  }else{
    $sql = "insert into cliente values (null,'".$cpf."','".$nome."') returning id;";
    $result = $conexao->query($sql)->fetchAll(2);
    $idCliente = $result[0]['id'];
  }

  var_dump($idCliente);
  $insert = "insert into passageiro values (null,'".$id ."','".$idCliente."') returning id;";
  $result= $conexao->query($insert)->fetcAll(2);
  $idPssageiro = $result[0]['id'];
  if ( $idPssageiro > 0 ){
    $resultado = ["status" => "true", "passagem" =>$idPssageiro ];
  } else {
    $resultado = ["status"=>"false"];
  };
  
  $txt = json_encode( $resultado );
  print $txt;
?>
