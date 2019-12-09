<template>
  <div>
    <b-container>
      <b-row>
        <b-col v-for="item of collect" :key="item.id" md="4"> 
          <b-card
          title="Card Title"
          img-src="https://st3.depositphotos.com/7852538/19409/i/1600/depositphotos_194096488-stock-photo-sweet-puppy-dogo-argentino-standing.jpg"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2"
          >
            <b-card-text>
              Some quick example text to build on the card title and make up the bulk of the card's content.
            </b-card-text>

            <b-button href="#" variant="primary">Go somewhere</b-button>

          </b-card>
        </b-col>
      </b-row>
    </b-container>
    

  </div>
</template>

<script>
export default {
  name: 'ListAdoption',

  data() {
    return {
      collect: [1,2,3,4,5,6,7,8,9,10,11,12]
    }
  },
}
</script>

