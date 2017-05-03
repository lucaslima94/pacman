#include <stdio.h>


void calcula(){
	float vetor[26];
	int cont = 0;
	char c;
	int i;
	int numero;
	FILE *arq;
	char* texto = "nome.txt";

	for(i = 0; i < 27; i++){
		vetor[i] = 0;
	}

	arq = fopen(texto, "rt");
	if(arq == NULL){
		printf("Problema na leitura");
		return;
	}
	while((c = getc(arq))!=	EOF){
		cont++;
		numero = (int)c;
		if(numero == 32){
			vetor[0]++;
		}
		else{
			if((numero > 64)&&(numero < 91)){
				vetor[numero-64]++;
			}
			
		}

	}
	for(i = 0; i < 27; i++){
		printf("Posicao: %d   ", i);
		printf("%f \n", vetor[i]);
		vetor[i] = (vetor[i]/cont)*100;
		printf("Posicao: %d   ", i);
		printf("%f \n", vetor[i]);
	}
	printf("Contador: %d", cont);
}

void main(){
	calcula();
}
