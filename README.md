# Mineração de Dados Avançada - 2023/1 - UFMG

Nesse repositório se encontra o trabalho desenvolvido e realizado na disciplina Mineração de Dados Avançada, da UFMG, no período de 2023/1.


# TO-DO

### TP

- Observações do Loic
    - `Prefiro pouco bem feito (boa metodologia, bem justificada, visualização e interpretação dos achados, etc.) a muitas coisas não tão bem feitas.  Em particular, prefiro um só modelo de regressão a vários, desde que vocês explicam bem como escolheram o modelo (vão testar vários), como validaram ele (evitando sobreajuste), com o cuidado de ver se tem pouca multicolinearidade antes de interpretar um estimador, talvez comentando as melhores/piores ofertas o site (preços previstos bem abaixo/acima do previsto pelo modelo, o que pode permitir de comentar limitações, como características não levada em conta pelo modelo), etc.`
    - Melhorias no Relatório
        - :heavy_check_mark: Enriquecer o contexto com dados sobre o crescimento nos preços de automóveis 
        - :heavy_check_mark: Definição de usado/seminovo
        - [Visualização] Discutir estatísticas (range, média, desvio padrão) dos preços médios dos carros (que aparentemente não seguem uma normal)
            - `como falei para vocês, não sei se a definição de outlier do boxplot é pertinente.  Parece mais que esses atributos têm distribuições com codas pesadas.  Talvez até distribuições em lei de potência.`
        - [Visualização] Discutir distribuição dos preços médios
            - Histograma ordenado na vertical
            - Verificar lei de potência
                - `Talvez a distribuição segue uma lei de potência e, neste caso, pode ser que a média e o desvio padrão não fazem sentido.  Uma lei de potência se caracteriza olhando o diagrama de dispersão dos pontos de abscissas log(ranqueamento do preço médio) (log(1) para o maior preço, log(2) para o segundo maior, etc.) e de ordenadas log(preço médio) (então necessariamente vai decrescendo).  Se, nesse diagrama, os pontos são alinhados (para ranques cobrindo três ordens de grandeza consecutivas) então vocês têm uma lei de potência.`
        - :heavy_check_mark: Escrever quando foram realizados os scrapings
        - :heavy_check_mark: Limitações da pesquisa
            - Carros de luxo não aparecem no site; carros desaparecem depois de 1 dia que são vendidos (mudou nosso foco para analisar os acessórios desejáveis e sua influência no preço dos anúncios)
        - `As tabelas tomam muito espaço.  Na versão final do relatório, vocês podem ignorar os atributos que nunca usam.`
    - Tarefas de mineração de dados que podemos realizar
        - Tirar o log dos preços e checar como fica a distribuição
        - Mineração de itemsets na coluna “acessórios”
            - `Para a mineração de itemsets, deixam como está: a maioria dos algoritmos de mineração de itemsets usam esse formato`
            - Mas, é útil mesmo obter a lista de 0 e 1 para a regressão.  Se vocês selecionam com cut a coluna com os acessórios presentes separados por vírgulas (claro, pode ser um outro separador) e redirecionam a saída para uma arquivo chamado acessórios, podem executar isso:
            `tr , \\n < acessórios | sort -u | gawk -F , 'ARGIND == 1 { att[++n] = $0 } ARGIND == 2 { for (i = 1; i <= n; ++i) { for (j = 1; $j != att[i] && j <= NF; ++j); printf "," (j <= NF) } print "" }' - acessórios | cut -c 2-`
            - `A mineração de itemsets frequentes pode servir a analisar os acessórios frequentemente juntos.  Podem definir uma função de qualidade do itemset que irá agregar o quão desejáveis os carros no suporte do itemset (talvez uma média aritmética das diferenças entre os preços e os preços da tabela FIPE ou dos preços previstos de um modelo de regressão que não envolve os acessórios), avaliar essa função para todos os itemsets frequentes e interpretar os itemsets que recebem os maiores valores.  Porém, parece meio óbvio que mais acessórios (no sentido da inclusão) é mais desejável.  Talvez podem dividir as avaliações pela soma das estimativas dos parâmetros associados a cada acessório no modelo de regressão.`
            - `Também podem minerar regras de associação.  Uma regra X -> Y de confiança c se interpreta "Uma proporção c dos carros com os acessórios em X tem os acessórios em Y".  As regras de associação X -> Y com confiança alta, enquanto Y -> X tem confiança baixa, indicam então uma especie de prioridade entre conjuntos de acessórios (possivelmente um só acessório por conjunto): Y são acessórios mais "essenciais" que X (poucos compram X sem ter também Y; enquanto o inverso é falso).`
        - Regressão linear por modelo de carro
            - `Com muitos atributos independentes e poucos carros (especialmente se vocês criam um modelo de regressão por modelo de carro: talvez seria melhor um modelo para compacto, um para sedan, uma para SUV, etc.: tem essas categorias?), pode haver sobreajuste: pode usar validação cruzada (que ensinarei quando apresentarei a classificação) para evitar isso, retirando os atributos menos úteis à predição.  Também pode haver multicolinearidade.  Impede a interpretação de estimativas de parâmetros (mas não é um problema para melhorar as predições).  Antes de interpretar uma tal estimativa, olhem o coeficiente de determinação do modelo que prevê o atributo correspondente a partir dos demais atributos explicativos.  Se for próximo de 1, não pode interpretar a estimativa.`
