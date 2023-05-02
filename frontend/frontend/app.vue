<template>
  <div class="container">
    <div id="menu-bar" class="menu-style">
      <div>
        <span>Icon</span>
        <a href="">CEL</a>
      </div>
      <div id="menu-itens">
        <a href="">Opção</a>
        <a href="">Cor</a>
        <a href="">Carrinho</a>
      </div>
    </div>
    
    <div>
      <input id="busca" placeholder="Título, autor, editora ...">
    </div>

    <h1>Idiomas</h1>
    <div id="seletor-idiomas">
      <div class="idioma"><img src="./images/spain.jpg" alt=""></div>
      <div class="idioma"><img src="./images/spain.jpg" alt=""></div>
      <div class="idioma"><img src="./images/spain.jpg" alt=""></div>
      <div class="idioma"><img src="./images/spain.jpg" alt=""></div>
    </div>

    <div id="novos-livros">
      <div class="livro">
        <img src="" alt="">
        <div>
          <h1>Título 1</h1>
          <h2>Subtítulo 1</h2>
        </div>
        <button></button>
      </div>
      <div>
        <img src="" alt="">
        <div>
          <h1></h1>
          <h2></h2>
        </div>
        <button></button>
      </div>
      <div>
        <img src="" alt="">
        <div>
          <h1></h1>
          <h2></h2>
        </div>
        <button></button>
      </div>
      <div>
        <img src="" alt="">
        <div>
          <h1></h1>
          <h2></h2>
        </div>
        <button></button>
      </div>
    </div>

    <div id="menu-navegação" class="menu-style">
      <a href="">A</a>
      <a href="">B</a>
      <a href="">C</a>
      <a href="">D</a>
    </div>
  </div>
</template>

<style scoped>
  *{
    margin: 0;
    text-decoration: none;
  }

  #container{
    width: 100vw;
    height: 100vh;
  }

  .menu-style{
    background-color: aqua;
    display: flex;
    padding: 10px;
  }

  #menu-bar{
    justify-content: space-between;
  }

  #menu-bar span{
    margin-right: 5px;
  }

  #menu-bar #menu-itens a{
    margin: 0 5px;
  }

  img{
    width: 20px;
  }

  #menu-navegação{
    justify-content: space-between;
  }
</style>
