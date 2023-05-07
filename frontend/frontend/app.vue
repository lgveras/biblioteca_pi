<template>
  <v-app class="justify-content-center align-items-center mb-6">
    <div id="menu-bar" class="menu-style color-menu">
      <div id="marker-menu">
        <v-icon>mdi-map-marker</v-icon>
        <a href="">CEL</a>
      </div>

      <div id="menu-itens">
        <v-btn density="compact" icon="mdi-cog" variant="text">
        </v-btn>
        <v-btn density="compact" icon="mdi-brightness-4" variant="text">
        </v-btn>
        <v-btn density="compact" icon="mdi-cart-outline" variant="text">
        </v-btn>
      </div>
    </div>

    <v-container fill-height style="margin: 0 auto">
      <v-col cols="12">
        <div id="menu-bar-pc" class="menu-style w-100 mb-10">
          <div id="title-menu" class="w-100">
            <div id="logo">
              <img src="@/images/cel_logo.jpg" alt="Logo do CEL">
            </div>
            <div id="title" class="color-menu">
              Sistema de Bibliotecas do CEL
            </div>
          </div>

          <div id="menu-btns">
            <v-btn class="color-menu btn-menu" prepend-icon="mdi-map-marker">
              Localização
            </v-btn>
            <v-btn class="color-menu btn-menu" prepend-icon="mdi-cog">
              Configuração
            </v-btn>
            <v-btn class="color-menu btn-menu" prepend-icon="mdi-cart-outline">
              Pedidos
            </v-btn>
            <v-btn class="color-menu btn-menu" prepend-icon="mdi-menu">
              Resenha
            </v-btn>
            <v-btn class="color-menu btn-menu" prepend-icon="mdi-heart">
              Favoritas
            </v-btn>
            <v-btn class="color-menu btn-menu" prepend-icon="mdi-account">
              Login/Usuário
            </v-btn>
          </div>
        </div>

        <div id="search-bar">
          <v-text-field class="mb-10" label="Título, autor, editora ..." hide-details="auto">
          <v-icon id="search-icon" class="pb-6" size="x-large" :icon="'mdi-magnify'" />
        </v-text-field>
        </div>
      

        <div id="language-selector" class="mb-10">
          <h1>Idiomas</h1>
          <v-carousel id="idiomas-carousel" hide-delimiters>
            <!-- Button to previous element -->
            <!-- <template v-slot:prev="{ props }">
            <v-btn variant="elevated" color="success" @click="props.onClick">Previous slide</v-btn>
          </template> -->
            <!-- Button to next element -->
            <!-- <template v-slot:next="{ props }">
            <v-btn @click="props.onClick">
              <v-icon :icon="'mdi-arrow'"></v-icon>
            </v-btn>
          </template> -->

            <v-carousel-item>
              <div onclick="alert('Clicou')" class="idioma"><img src="./images/spain.jpg" alt=""></div>
            </v-carousel-item>
            <v-carousel-item>
              <div class="idioma"><img src="./images/spain.jpg" alt=""></div>
            </v-carousel-item>
            <v-carousel-item>
              <div class="idioma"><img src="./images/spain.jpg" alt=""></div>
            </v-carousel-item>
          </v-carousel>
        </div>

        <div id="new-books" style="max-width: 100vw;" theme="dark">
          <h1 class="mb-3">Novos Livros</h1>
          <div id="list-new-books">
            <v-card class="mx-auto mb-2">
              <div class="d-flex flex-no-wrap justify-space-between">
                <div class="book-item">
                  <img src="@/images/cover-decartes.jpg" alt="Capa do Livro">
                </div>
                <div class="d-flex flex-column justify-space-between">
                  <div>
                    <v-card-title class="text-h5 text-wrap">
                      O dircurso do método
                    </v-card-title>
                    <v-card-subtitle>René Descartes</v-card-subtitle>
                  </div>
                  <v-card-actions class="action-book">
                    <v-btn density="comfortable" class="ms-1" size="x-small" prepend-icon="mdi-plus" stacked
                      variant="tonal"></v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>

            <v-card class="mx-auto mb-2">
              <div class="d-flex  flex-no-wrap justify-space-between">
                <div class="book-item">
                  <img src="@/images/cover-decartes.jpg" alt="Capa do Livro">
                </div>
                <div class="d-flex flex-column justify-space-between">
                  <div>
                    <v-card-title class="text-h5 text-wrap">
                      O dircurso do método
                    </v-card-title>
                    <v-card-subtitle>Rene Decartes</v-card-subtitle>
                  </div>
                  <v-card-actions class="action-book">
                    <v-btn density="comfortable" class="ms-1" size="x-small" prepend-icon="mdi-plus" stacked
                      variant="tonal"></v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>

            <v-card class="mx-auto mb-2">
              <div class="d-flex flex-no-wrap justify-space-between">
                <div class="book-item">
                  <img src="@/images/cover-decartes.jpg" alt="Capa do Livro">
                </div>
                <div class="d-flex flex-column justify-space-between">
                  <div>
                    <v-card-title class="text-h5 text-wrap">
                      O dircurso do método
                    </v-card-title>
                    <v-card-subtitle>Rene Decartes</v-card-subtitle>
                  </div>
                  <v-card-actions class="action-book">
                    <v-btn density="comfortable" class="ms-1" size="x-small" prepend-icon="mdi-plus" stacked
                      variant="tonal"></v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>
          </div>
        </div>

        <v-bottom-navigation grow class="menu-style bottom-navigation">
          <v-btn value="recent">
            <v-icon>mdi-home</v-icon>
            Home
          </v-btn>

          <v-btn value="recent">
            <v-icon>mdi-menu</v-icon>
            Opções
          </v-btn>

          <v-btn value="favorites">
            <v-icon>mdi-heart</v-icon>
            Favoritos
          </v-btn>

          <v-btn value="nearby">
            <v-icon>mdi-account</v-icon>
            Cadastro
          </v-btn>
        </v-bottom-navigation>
      </v-col>
    </v-container>

  </v-app>
</template>

<style scoped>
* {
  margin: 0;
  text-decoration: none;
  box-sizing: border-box;
}

h1,
h2 {
  font-family: 'Roboto', sans-serif;
}

.menu-style {
  display: flex;
}

.color-menu {
  background-color: aqua;
}

#search-icon {
  position: absolute;
  right: 10px;
}

img {
  max-width: 80%;
}

.action-book {
  align-self: flex-end;
}

@media screen and (max-width: 375px) {
  .menu-style {
    padding: 10px;
  }

  #menu-bar-pc {
    display: none;
  }

  #menu-bar {
    justify-content: space-between;
    display: relative;
    left: 0;
    width: 100vw;
  }

  #marker-menu {
    display: flex;
    align-items: center;
  }

  #menu-bar span {
    margin-right: 5px;
  }

  #menu-bar #menu-itens * {
    margin: 0 5px;
  }

  #menu-navegação {
    justify-content: space-between;
  }

  #idiomas-carousel {
    height: 100px !important;
  }

  .idioma {
    width: 100px;
  }

  .book-item {
    margin-left: 10px;
    max-width: 198px;
    display: grid;
    place-content: center;
  }
}

@media screen and (min-width: 375px) {
  h1 {
    font-size: 3rem;
  }

  #menu-bar {
    display: none;
  }

  .menu-style {
    flex-direction: column;
    gap: 10px
  }

  #logo {
    max-width: 50px;
  }

  #logo>img {
    max-width: inherit;
  }

  #title-menu {
    flex: 1 1 auto;
    display: flex;
    text-align: center;
    gap: 30px
  }

  #title-menu #title {
    width: inherit;
    display: grid;
    place-content: center;
    font-weight: bold;
    font-size: 2rem;
  }

  #menu-btns {
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-between;
    gap: 20px
  }

  #menu-btns>.btn-menu {
    font-size: x-small;
    flex-shrink: 1;
  }

  #search-bar {
    width: 40%;
    margin: 0 auto;
  }

  #language-selector {
    text-align: center;
    width: 50%;
    margin: 0 auto;
  }

  #idiomas-carousel {
    height: 160px !important;
  }

  #idiomas-carousel .idioma {
    width: 200px;
  }

  #new-books h1 {
    text-align: center;
  }

  #list-new-books {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    column-gap: 20px;
  }

  .book-item {
    margin: 20px;
    max-width: 198px;
    display: grid;
    place-content: center;
  }

  .bottom-navigation {
    display: none;
  }
}</style>