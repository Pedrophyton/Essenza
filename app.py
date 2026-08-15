from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Essenza | Massoterapia Personalizada</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            background: #f3fffc;
            color: #294d46;
        }

        header {
            background: #5bc7b2;
            color: white;
            padding: 20px 7%;

            display: flex;
            justify-content: space-between;
            align-items: center;

            box-shadow: 0 3px 15px rgba(0,0,0,0.10);
        }

        .logo {
            font-size: 30px;
            font-weight: bold;
            letter-spacing: 3px;
        }

        .header-text {
            font-size: 14px;
        }

        .hero {
            text-align: center;
            padding: 60px 20px 40px;
        }

        .hero h1 {
            color: #278f7c;
            font-size: 40px;
            margin-bottom: 15px;
        }

        .hero p {
            max-width: 700px;
            margin: auto;

            color: #617a74;
            line-height: 1.7;
            font-size: 16px;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: auto;
        }

        .box {
            background: white;
            padding: 30px;
            border-radius: 20px;

            box-shadow: 0 6px 25px rgba(0,0,0,0.07);

            margin-bottom: 30px;
        }

        .box h2 {
            color: #278f7c;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 18px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 7px;
        }

        input {
            width: 100%;
            padding: 14px;

            border: 1px solid #b8ded7;
            border-radius: 10px;

            font-size: 15px;
            outline: none;
        }

        input:focus {
            border-color: #5bc7b2;
            box-shadow: 0 0 0 3px rgba(91,199,178,0.15);
        }

        button {
            border: none;
            cursor: pointer;

            border-radius: 10px;
            padding: 14px 20px;

            font-size: 16px;
            font-weight: bold;

            transition: 0.2s;
        }

        .btn-primary {
            width: 100%;

            background: #5bc7b2;
            color: white;
        }

        .btn-primary:hover {
            background: #43b29d;
        }

        #personalizacao {
            display: none;
        }

        .section-title {
            text-align: center;
            margin-bottom: 30px;
        }

        .section-title h2 {
            color: #278f7c;
            font-size: 30px;
            margin-bottom: 8px;
        }

        .section-title p {
            color: #687f79;
        }

        .grid {
            display: grid;

            grid-template-columns: repeat(2, 1fr);

            gap: 22px;
        }

        .card {
            background: white;

            padding: 25px;

            border-radius: 18px;

            box-shadow: 0 5px 20px rgba(0,0,0,0.07);

            border-top: 5px solid #8bdccd;
        }

        .card h3 {
            color: #278f7c;
            font-size: 22px;

            margin-bottom: 10px;
        }

        .description {
            color: #647c76;

            line-height: 1.5;

            margin-bottom: 18px;
        }

        .options {
            display: grid;
            gap: 10px;
        }

        .option {
            padding: 14px;

            background: #f5fffc;

            border: 2px solid #d7eee9;

            border-radius: 10px;

            cursor: pointer;

            transition: 0.2s;
        }

        .option:hover {
            border-color: #5bc7b2;
        }

        .option.selected {
            background: #5bc7b2;
            border-color: #5bc7b2;

            color: white;

            font-weight: bold;
        }

        .info {
            background: #effbf8;

            padding: 17px;

            border-radius: 12px;

            margin-top: 20px;

            line-height: 1.6;

            font-size: 14px;
        }

        .info strong {
            color: #278f7c;
        }

        .resumo {
            margin-top: 30px;

            background: white;

            padding: 30px;

            border-radius: 20px;

            box-shadow: 0 6px 25px rgba(0,0,0,0.07);
        }

        .resumo h2 {
            color: #278f7c;

            margin-bottom: 20px;
        }

        .resumo-item {
            padding: 12px 0;

            border-bottom: 1px solid #e4f1ee;
        }

        .resumo-item:last-child {
            border-bottom: none;
        }

        .whatsapp {
            margin-top: 25px;
        }

        .whatsapp h3 {
            color: #278f7c;
            margin-bottom: 8px;
        }

        .whatsapp p {
            color: #687f79;

            margin-bottom: 15px;

            line-height: 1.5;
        }

        .btn-whatsapp {
            width: 100%;

            background: #45b894;

            color: white;
        }

        .btn-whatsapp:hover {
            background: #359779;
        }

        .erro {
            color: #c0392b;

            font-size: 14px;

            margin-top: 10px;
        }

        footer {
            margin-top: 60px;

            padding: 35px 20px;

            background: #278f7c;

            color: white;

            text-align: center;
        }

        footer strong {
            font-size: 20px;

            letter-spacing: 2px;
        }

        footer p {
            margin-top: 10px;

            font-size: 13px;

            opacity: 0.85;
        }

        @media (max-width: 700px) {

            header {
                flex-direction: column;
                gap: 8px;

                text-align: center;
            }

            .hero h1 {
                font-size: 30px;
            }

            .grid {
                grid-template-columns: 1fr;
            }

            .box,
            .card,
            .resumo {
                padding: 22px;
            }

        }

    </style>

</head>


<body>


<header>

    <div class="logo">
        ESSENZA
    </div>

    <div class="header-text">
        Massoterapia personalizada
    </div>

</header>


<section class="hero">

    <h1>
        Seu momento de relaxamento
    </h1>

    <p>
        Personalize o ambiente da sua sessão de massoterapia
        escolhendo temperatura, música, aroma e iluminação.
    </p>

</section>


<div class="container">


    <!-- CADASTRO -->

    <section class="box">

        <h2>
            Cadastro do cliente
        </h2>


        <div class="form-group">

            <label>
                Nome
            </label>

            <input
                type="text"
                id="nome"
                placeholder="Digite seu nome"
            >

        </div>


        <div class="form-group">

            <label>
                E-mail
            </label>

            <input
                type="email"
                id="email"
                placeholder="Digite seu e-mail"
            >

        </div>


        <button
            class="btn-primary"
            onclick="iniciar()"
        >
            Continuar
        </button>

    </section>



    <!-- PERSONALIZAÇÃO -->

    <section id="personalizacao">


        <div class="section-title">

            <h2>
                Personalize sua experiência
            </h2>

            <p>
                Escolha uma opção em cada categoria.
            </p>

        </div>


        <div class="grid">


            <!-- TEMPERATURA -->

            <div class="card">

                <h3>
                    🌡️ Temperatura
                </h3>

                <p class="description">
                    Escolha a temperatura preferida
                    para o ambiente.
                </p>


                <div class="options">

                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'temperatura',
                            '16°C'
                        )"
                    >
                        16°C
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'temperatura',
                            '20°C'
                        )"
                    >
                        20°C
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'temperatura',
                            '28°C'
                        )"
                    >
                        28°C
                    </div>

                </div>


                <div class="info">

                    <strong>
                        Importância:
                    </strong>

                    proporciona maior conforto
                    durante a sessão.

                    <br><br>

                    <strong>
                        Terapia:
                    </strong>

                    auxilia na criação de um ambiente
                    adequado ao relaxamento.

                    <br><br>

                    <strong>
                        Sistema nervoso:
                    </strong>

                    um ambiente confortável pode favorecer
                    uma sensação de tranquilidade.

                </div>

            </div>



            <!-- MUSICA -->

            <div class="card">

                <h3>
                    🎵 Música
                </h3>

                <p class="description">
                    Escolha os sons que acompanharão
                    sua sessão.
                </p>


                <div class="options">

                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'musica',
                            'Calmas/relaxantes'
                        )"
                    >
                        Calmas/relaxantes
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'musica',
                            'Sons de natureza'
                        )"
                    >
                        Sons de natureza
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'musica',
                            'Sem música'
                        )"
                    >
                        Sem música
                    </div>

                </div>


                <div class="info">

                    <strong>
                        Importância:
                    </strong>

                    ajuda a criar uma atmosfera
                    agradável.

                    <br><br>

                    <strong>
                        Terapia:
                    </strong>

                    pode complementar técnicas
                    de relaxamento.

                    <br><br>

                    <strong>
                        Sistema nervoso:
                    </strong>

                    sons suaves podem contribuir
                    para uma sensação de calma.

                </div>

            </div>



            <!-- AROMA -->

            <div class="card">

                <h3>
                    🌿 Aroma
                </h3>

                <p class="description">
                    Escolha a essência utilizada
                    no ambiente.
                </p>


                <div class="options">

                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'aroma',
                            'Essência de Lavanda'
                        )"
                    >
                        Essência de Lavanda
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'aroma',
                            'Essência de Camomila'
                        )"
                    >
                        Essência de Camomila
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'aroma',
                            'Essência de Capim-limão'
                        )"
                    >
                        Essência de Capim-limão
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'aroma',
                            'Essência de Eucalipto'
                        )"
                    >
                        Essência de Eucalipto
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'aroma',
                            'Essência de Alecrim'
                        )"
                    >
                        Essência de Alecrim
                    </div>

                </div>


                <div class="info">

                    <strong>
                        Importância:
                    </strong>

                    acrescenta uma experiência
                    sensorial ao ambiente.

                    <br><br>

                    <strong>
                        Terapia:
                    </strong>

                    a aromaterapia utiliza aromas
                    como complemento ao bem-estar.

                    <br><br>

                    <strong>
                        Sistema nervoso:
                    </strong>

                    alguns aromas podem contribuir
                    para uma sensação de relaxamento.

                </div>

            </div>



            <!-- LUZ -->

            <div class="card">

                <h3>
                    💡 Intensidade e cor da luz
                </h3>

                <p class="description">
                    Escolha a atmosfera luminosa
                    do ambiente.
                </p>


                <div class="options">

                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'luz',
                            'Cores neutras'
                        )"
                    >
                        Cores neutras
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'luz',
                            'Cores quentes'
                        )"
                    >
                        Cores quentes
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'luz',
                            'Luz média'
                        )"
                    >
                        Luz média
                    </div>


                    <div
                        class="option"
                        onclick="selecionar(
                            this,
                            'luz',
                            'Luz baixa'
                        )"
                    >
                        Luz baixa
                    </div>

                </div>


                <div class="info">

                    <strong>
                        Importância:
                    </strong>

                    ajuda a definir a atmosfera
                    do ambiente.

                    <br><br>

                    <strong>
                        Terapia:
                    </strong>

                    pode complementar um ambiente
                    voltado ao relaxamento.

                    <br><br>

                    <strong>
                        Sistema nervoso:
                    </strong>

                    uma iluminação confortável pode
                    favorecer sensação de descanso.

                </div>

            </div>


        </div>



        <!-- RESUMO -->

        <div class="resumo">

            <h2>
                Resumo da sessão
            </h2>


            <div class="resumo-item">

                <strong>
                    Cliente:
                </strong>

                <span id="rNome">
                    -
                </span>

            </div>


            <div class="resumo-item">

                <strong>
                    Temperatura:
                </strong>

                <span id="rTemperatura">
                    Não escolhida
                </span>

            </div>


            <div class="resumo-item">

                <strong>
                    Música:
                </strong>

                <span id="rMusica">
                    Não escolhida
                </span>

            </div>


            <div class="resumo-item">

                <strong>
                    Aroma:
                </strong>

                <span id="rAroma">
                    Não escolhido
                </span>

            </div>


            <div class="resumo-item">

                <strong>
                    Luz:
                </strong>

                <span id="rLuz">
                    Não escolhida
                </span>

            </div>



            <!-- WHATSAPP -->

            <div class="whatsapp">

                <h3>
                    📲 Enviar para o massoterapeuta
                </h3>

                <p>
                    Digite o número do WhatsApp do
                    massoterapeuta com o código do país.
                </p>


                <input
                    type="tel"
                    id="telefone"
                    placeholder="Ex.: 5588999999999"
                >


                <button
                    class="btn-whatsapp"
                    onclick="enviarWhatsApp()"
                >
                    Enviar escolhas pelo WhatsApp
                </button>


                <p
                    id="erro"
                    class="erro"
                ></p>

            </div>

        </div>


    </section>


</div>



<footer>

    <strong>
        ESSENZA
    </strong>

    <p>
        Massoterapia personalizada.
    </p>

    <p>
        As informações apresentadas são gerais
        e não substituem orientação profissional.
    </p>

</footer>



<script>

    const escolhas = {

        temperatura: "",

        musica: "",

        aroma: "",

        luz: ""

    };


    function iniciar() {

        const nome =
            document
                .getElementById("nome")
                .value
                .trim();


        const email =
            document
                .getElementById("email")
                .value
                .trim();


        if (nome === "") {

            alert("Digite seu nome.");

            return;

        }


        if (email === "") {

            alert("Digite seu e-mail.");

            return;

        }


        document
            .getElementById("rNome")
            .textContent = nome;


        document
            .getElementById("personalizacao")
            .style.display = "block";


        document
            .getElementById("personalizacao")
            .scrollIntoView({
                behavior: "smooth"
            });

    }



    function selecionar(
        elemento,
        categoria,
        valor
    ) {


        const opcoes =
            elemento
                .parentElement
                .querySelectorAll(".option");


        opcoes.forEach(
            function(opcao) {

                opcao.classList.remove(
                    "selected"
                );

            }
        );


        elemento.classList.add(
            "selected"
        );


        escolhas[categoria] = valor;


        if (
            categoria === "temperatura"
        ) {

            document
                .getElementById("rTemperatura")
                .textContent = valor;

        }


        if (
            categoria === "musica"
        ) {

            document
                .getElementById("rMusica")
                .textContent = valor;

        }


        if (
            categoria === "aroma"
        ) {

            document
                .getElementById("rAroma")
                .textContent = valor;

        }


        if (
            categoria === "luz"
        ) {

            document
                .getElementById("rLuz")
                .textContent = valor;

        }

    }



    function enviarWhatsApp() {


        const nome =
            document
                .getElementById("nome")
                .value
                .trim();


        const email =
            document
                .getElementById("email")
                .value
                .trim();


        const telefone =
            document
                .getElementById("telefone")
                .value
                .trim();


        const erro =
            document
                .getElementById("erro");


        erro.textContent = "";


        if (telefone === "") {

            erro.textContent =
                "Digite o número do massoterapeuta.";

            return;

        }


        if (
            escolhas.temperatura === "" ||
            escolhas.musica === "" ||
            escolhas.aroma === "" ||
            escolhas.luz === ""
        ) {

            erro.textContent =
                "Escolha uma opção em cada categoria.";

            return;

        }


        // Mantém somente números

        const numero =
            telefone.replace(
                /\\D/g,
                ""
            );


        if (numero.length < 10) {

            erro.textContent =
                "Digite um número válido com DDD e código do país.";

            return;

        }


        const mensagem =

`Olá! Sou ${nome}.

Gostaria de informar minhas preferências para minha sessão de massoterapia na Essenza.

🌡️ Temperatura: ${escolhas.temperatura}

🎵 Música: ${escolhas.musica}

🌿 Aroma: ${escolhas.aroma}

💡 Luz: ${escolhas.luz}

📧 E-mail: ${email}

Obrigado!`;


        const url =

            "https://wa.me/" +
            numero +
            "?text=" +
            encodeURIComponent(
                mensagem
            );


        window.open(
            url,
            "_blank"
        );

    }

</script>


</body>

</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
