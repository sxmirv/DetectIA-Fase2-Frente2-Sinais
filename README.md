# DetectIA Fase 2 · Frente 2 (Sinais)

**Pergunta da frente:** que rastros um gerador deixa na imagem, e quanto
deles sobrevive até chegar ao celular de alguém?

## Linhas de investigação
- A: Fourier e espectro médio
- B: DCT e efeito do JPEG
- C: Wavelets e resíduos

## Regras do projeto
- Recorte central, nunca resize (resize altera o espectro)
- Espectro sempre com fftshift e log1p(|F|)
- Antes de concluir algo, checar formato (PNG/JPEG) e resolução
- Todo experimento entra no log.md

## Como rodar
    pip install -r requirements.txt

## Dados
Não versionados. Origem em data/README.md.
