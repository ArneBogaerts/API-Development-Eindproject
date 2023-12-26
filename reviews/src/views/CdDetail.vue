<template>
  <div class="cd-details-container">
    <p>Reviews:</p>
    <ul class="reviews-list" v-if="cdDetails.length">
      <li v-for="review in reviews" :key="review.id" class="review-item">
        <strong>{{ review.rating }}:</strong> {{ review.comment }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cdDetails: null,
      reviews: [],
    };
  },
  created() {
    this.fetchCDDetails();
    this.fetchReviews();
  },
  methods: {
    async fetchCDDetails() {
      const cdId = this.$route.params.id;
      const url = `${process.env.VUE_APP_BACKEND_URL}/cds/${cdId}/reviews/?skip=0&limit=10`;
      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        this.cdDetails = await response.json();
      } catch (error) {
        console.error("There was a problem fetching the CD details:", error);
      }
    },
    async fetchReviews() {
      const cdId = this.$route.params.id;
      const reviewsUrl = `${process.env.VUE_APP_BACKEND_URL}/cds/${cdId}/reviews/?skip=0&limit=10`;
      try {
        const response = await fetch(reviewsUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        this.reviews = await response.json();
      } catch (error) {
        console.error("There was a problem fetching the reviews:", error);
      }
    }
  },
};
</script>

<style scoped>
.cd-details-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 8px;
}

.reviews-list {
  list-style-type: none;
  padding-left: 0;
}

.review-item {
  background-color: #fff;
  padding: 10px;
  margin-bottom: 8px;
  border-left: 3px solid #3498db;
}

h2 {
  color: #2c3e50;
}
</style>
