<template>
  <v-app>

    <v-container>
      <div id="menu-bar" class="menu-style">
        <div id="marker-menu">
          <v-icon>mdi-map-marker</v-icon>
          <a href="">CEL</a>
        </div>
        <div id="menu-itens">
          <v-btn density="compact" icon="mdi-brightness-4" variant="text">
          </v-btn>
          <v-btn density="compact" icon="mdi-cog" variant="text">
          </v-btn>
          <v-btn density="compact" icon="mdi-cart-outline" variant="text">
          </v-btn>
        </div>
      </div>

      <v-text-field class="search-bar" label="Título, autor, editora ..." hide-details="auto">
        <v-icon id="search-icon" class="pb-6" size="x-large" :icon="'mdi-magnify'" />
      </v-text-field>

      <h1>Idiomas</h1>
      <div id="language-selector">
        <v-carousel height="100" hide-delimiters>
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

      <div id="new-books" theme="dark">
        <h1>Novos Livros</h1>
        <div>
          <v-card class="mx-auto mb-2">
            <div class="d-flex flex-no-wrap justify-space-between">
              <div class="ma-3 book-item">
                <img src="@/images/cover-decartes.jpg" alt="Capa do Livro">
              </div>
              <div class="d-flex flex-column justify-space-between">
                <div>
                  <v-card-title class="text-h5">
                    O dircurso do método
                  </v-card-title>
                  <v-card-subtitle>Rene Decartes</v-card-subtitle>
                </div>
                <v-card-actions class="action-book">
                  <v-btn class="ms-1" size="x-small" prepend-icon="mdi-plus" stacked variant="tonal"></v-btn>
                </v-card-actions>
              </div>
            </div>
          </v-card>

          <v-card class="mx-auto mb-2">
            <div class="d-flex flex-no-wrap justify-space-between">
              <div class="ma-3 book-item">
                <img src="@/images/cover-decartes.jpg" alt="Capa do Livro">
              </div>
              <div class="d-flex flex-column justify-space-between">
                <div>
                  <v-card-title class="text-h5">
                    O dircurso do método
                  </v-card-title>
                  <v-card-subtitle>Rene Decartes</v-card-subtitle>
                </div>
                <v-card-actions class="action-book">
                  <v-btn class="ms-1" size="x-small" prepend-icon="mdi-plus" stacked variant="tonal"></v-btn>
                </v-card-actions>
              </div>
            </div>
          </v-card>
        </div>
      </div>

      <v-bottom-navigation grow class="menu-style">
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
    </v-container>
  </v-app>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');

* {
  margin: 0;
  text-decoration: none;
}

h1,
h2 {
  font-family: 'Roboto', sans-serif;
}

.menu-style {
  background-color: aqua;
  display: flex;
  padding: 10px;
}

#menu-bar {
  justify-content: space-between;
}

#marker-menu{
  display: flex;
  align-items: center;
}

#menu-bar span {
  margin-right: 5px;
}

#menu-bar #menu-itens * {
  margin: 0 5px;
}

img {
  width: 100px;
}

#menu-navegação {
  justify-content: space-between;
}

.search-bar {
  margin: 20px 15px;
}

#search-icon {
  position: absolute;
  right: 10px;
}

#language-selector {
  margin-bottom: 20px;
}

.book-item {
  max-height: 196px;
}

.action-book {
  align-self: flex-end;
}
</style>
