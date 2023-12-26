<template>
  <div class="cd-list-container">
    <h1>CD List</h1>
    <ul class="cd-list">
      <li v-for="cd in cds" :key="cd.id" class="cd-item" @click="goToDetail(cd.id)">
        <span class="cd-title">{{ cd.title }}</span> by <span class="cd-artist">{{ cd.artist.name }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cds: [],
    };
  },
  mounted() {
    console.log(process.env);
    this.fetchCDs();
  },
  methods: {
    async fetchCDs() {
      const url = `${process.env.VUE_APP_BACKEND_URL}/cds/?skip=0&limit=10`;
      console.log('Fetching from URL:', url);

      try {
        const response = await fetch(url, {
          headers: {
            'accept': 'application/json'
          }
        });
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        this.cds = await response.json();
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
      }
    },
    goToDetail(id){
      this.$router.push({ name: 'CDDetails', params: { id }});
    }
  },
};
</script>

<style scoped>
.cd-list-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.cd-list {
  list-style: none;
  padding: 0;
}

.cd-item {
  background-color: #ffffff;
  padding: 10px 15px;
  margin-bottom: 10px;
  border-radius: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
  cursor: pointer;
}

.cd-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.cd-title {
  font-weight: bold;
  color: #333;
}

.cd-artist {
  color: #666;
}

h1 {
  text-align: center;
  color: #333;
}
</style>