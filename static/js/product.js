const getItems = () => ({
  colors: [],
  sizes: [],
  currentImage: {},
  selectedColor: null,
  selectedSize: null,

  init() {
    this.getData()
  },

  getData() {
    axios.get('/api/v1/product/colors/')
      .then(response => {
        this.colors = response.data
      })
  },

  getSize(color) {
    axios.get(`/api/v1/product/${color}/sizes/`)
      .then(response => {
        this.sizes = response.data
        this.selectedColor = color
      })
  },

  getProductImage(size) {
    this.selectedSize = size.size
    axios.get(`/api/v1/product/${this.selectedColor}/${this.selectedSize}/image/`)
      .then(response => {
        this.currentImage = response.data
      })
  },
})