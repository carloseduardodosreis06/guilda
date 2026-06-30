```javascript
// Comportamentos Globais de Interação do GuildControl
document.addEventListener("DOMContentLoaded", function () {
    console.log("✓ Scripts globais do GuildControl carregados.");

    // Exemplo de efeito ao passar o mouse em botões
    const botoes = document.querySelectorAll(".btn-primary");
    botoes.forEach(botao => {
        botao.addEventListener("click", function () {
            // Adiciona uma animação simples de clique se necessário
            this.style.transform = "scale(0.98)";
            setTimeout(() => {
                this.style.transform = "none";
            }, 100);
        });
    });
});

// Função global auxiliar para formatação de telefone caso use nos inputs
function mascaraTelefone(input) {
    let valor = input.value.replace(/\D/g, "");
    if (valor.length > 11) valor = valor.slice(0, 11);
    
    if (valor.length > 6) {
        input.value = `(${valor.slice(0, 2)}) ${valor.slice(2, 7)}-${valor.slice(7)}`;
    } else if (valor.length > 2) {
        input.value = `(${valor.slice(0, 2)}) ${valor.slice(2)}`;
    } else {
        input.value = valor;
    }
}
```

