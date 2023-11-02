const getItems = () => ({
  filteredItems: [],
  sizes: ['P', 'M', 'G', 'GG'],
  currentImage: '',

  init() {
    this.getData()
  },

  getData() {
    axios.get('/api/v1/product')
      .then(response => {
        const image = response.data[0].image[0].image
        this.currentImage = `http://localhost:8000/${image}`
        this.filteredItems = response.data
      })
  },

  getProduct(size, productId) {
    axios.get(`/api/v1/product/${productId}/image/${size.size}`)
      .then(response => {
        this.currentImage = response.data[0].image
      })
  },

  getImageColor(color, productId) {
    axios.get(`/api/v1/product/${productId}/color/${color.color}`)
      .then(response => {
        this.currentImage = response.data[0].image
      })
  },
})