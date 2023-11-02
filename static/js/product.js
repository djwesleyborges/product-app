const getItems = () => ({
  image: '',
  filteredItems: [],
  sizes: ['P', 'M', 'G', 'GG'],
  currentImage: '',

  init() {
    this.getData()
  },

  getData() {
    axios.get('/api/v1/product')
      .then(response => {
        this.image = response.data[0].image[0].image
        this.filteredItems = response.data
      })
  },

  getProduct(size, productId) {
    axios.get(`/api/v1/product/${productId}/image/${size.size}`)
      .then(response => {
        this.currentImage = response.data[0].image
        document.getElementById("imgChange").src = this.currentImage
      })
  },

  getImageColor(color, productId) {
    axios.get(`/api/v1/product/${productId}/color/${color.color}`)
      .then(response => {
        this.currentImage = response.data[0].image
        document.getElementById("imgChange").src = this.currentImage
      })
  },
})