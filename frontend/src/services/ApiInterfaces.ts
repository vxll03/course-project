interface IAuthor {
  name: string
  text: string
  bookCount: number
}

interface IBook {
  title: string
  text: string
  price: number
  img: string | null
}

export type { IAuthor, IBook }