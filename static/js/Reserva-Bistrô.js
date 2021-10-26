var n = 1;
var vazio = 1;
var add = document.getElementById("mais");
var clean = document.getElementById("limpar");

var valor = 85;

add.addEventListener("click", function(){
    n=n+1;
    var x = '<div id="reserva '+n+'" class="col-md-8 order-md-1"> <div class="row"> <h4 for="reserva" class="mb-3"> Reserva '+n+' </h4> </div> <div class="row"> <div class="col-md-6 mb-3"> <label for="primeiroNome">Nome</label> <input type="text" class="form-control" id="primeiro Nome" placeholder value required> <div class="invalid-feedback">É obrigatório inserir um nome válido.</div> </div> <div class="col-md-6 mb-3"> <label for="sobrenome">Sobrenome</label> <input type="text" class="form-control" id="sobrenome" placeholder value required> <div class="invalid-feedback">É obrigatório inserir um sobrenome válido.</div> </div> <div class="col-md-6 mb-3"> <label for="cpf">CPF</label> <input type="text" class="form-control" id="cpf" placeholder value required> <div class="invalid-feedback">É obrigatório inserir um CPF válido.</div> </div> <div class="col-md-6 mb-3"> <label for="cel">Telefone</label> <input type="text" class="form-control" id="telefone" placeholder value required> <div class="invalid-feedback">É obrigatório inserir um número de telefone válido.</div> </div> </div> <div class="row"> <div class="mb-3"> <label for="restriçoes"> Restrições <span class="text-muted">(Opcional)</span> </label> <div> <label for="intolerancias"> Intolerâncias: </label> <div class="form-check"> <input type="checkbox" class="form-check-input" id="intolerancias"> <label class="form-check-label" for="intolerancias"> <font style="vertical-align: inherit;">ao glúten</font> </label> </div> <div class="form-check"> <input type="checkbox" class="form-check-input" id="intolerancias"> <label class="form-check-label" for="intolerancias"> <font style="vertical-align: inherit;">à lactose</font> </label> </div> <div class="form-check"> <input type="checkbox" class="form-check-input" id="intolerancias"> <label class="form-check-label" for="intolerancias"> <font style="vertical-align: inherit;">vegano</font> </label> </div> <div class="form-check"> <input type="checkbox" class="form-check-input" id="intolerancias"> <label class="form-check-label" for="intolerancias"> <font style="vertical-align: inherit;">vegetariano</font> </label> </div> <div class="form-check"> <input type="checkbox" class="form-check-input" id="intolerancias"> <label class="form-check-label" for="intolerancias"> <font style="vertical-align: inherit;">Outra:<input type="text" class="form-control" id="Outra" placeholder="Cite aqui sua intolerância"></font> </label> </div> </div> </div> </div> </div> <div id="vazio'+n+'"> </div>';
    document.getElementById("vazio"+vazio).innerHTML += x;
    document.getElementById("preço").innerHTML = valor*n;
    clean.style.display="inline";
    vazio=vazio+1;
    
});

clean.addEventListener("click", function(){
    var node = document.getElementById("vazio1")
        if(node.parentNode){
            node.parentNode.removeChild(node);
        }
    n=1;
    vazio=1;
    document.getElementById("id_form").innerHTML += '<div id="vazio'+n+'"> </div>';
    document.getElementById("preço").innerHTML = valor*n;

    clean.style.display="none";
});




