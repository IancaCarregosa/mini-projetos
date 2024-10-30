
let faturamentoMensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "outros": 19849.53
};

let totalMensal = Object.values(faturamentoMensal).reduce((acc , val) => val + acc, 0)
for (let estado in faturamentoMensal){
    let porcentagem = (faturamentoMensal[estado]/totalMensal) *100;
    console.log(`O percentual de ${estado} é ${porcentagem.toFixed(2)}%`)
}