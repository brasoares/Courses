alert('Boas-vindas ao jogo do número secreto');
let numeroSecreto = 9;
console.log(numeroSecreto)
let chute = prompt('Escolha um número entre 1 e 10');

// Se o chute for menor ou igual ao número secreto:
if (chute == numeroSecreto) {
	alert(`Isso aí!Você descobriu o número secreto $ {
				numeroSecreto
			}, parabéns!`);
} else {
  alert('Você não acertou desta vez; tentar novamente!');
}
