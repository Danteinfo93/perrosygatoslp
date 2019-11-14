<template>
  <div id="app">
    <b-navbar toggleable="lg" type="light" style="background-color:#7DCEA0 ">
      <b-navbar-brand :to="{name:'home'}"><strong>PerrosygatosLP</strong></b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{name:'adoptions'}"><strong>Adopciónes</strong></b-nav-item>
          <b-nav-item :to="{name:'strayings'}"><strong>Extravios</strong></b-nav-item>
          <b-nav-item :to="{name:'findings'}"><strong>Hallazgos</strong></b-nav-item>
          <b-nav-item :to="{name:'trainers'}"><strong>Adiestradores</strong></b-nav-item>
          <b-nav-item :to="{name:'ads'}"><strong>Anuncios</strong></b-nav-item>
          <b-nav-item :to="{name:'crosses'}"><strong>Cruzas</strong></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items  #9e995d-->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Perfil</b-dropdown-item>
            <b-dropdown-item href="#">Ingresar</b-dropdown-item>
            <b-dropdown-item href="#">Registrarse</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <b-container>
      <router-view/>
    </b-container>
  </div>
</template>

