interface IAuthor {
  name: string
  text?: string
  bookCount: number
}

interface IBook {
  id: number
  title: string
  text: string
  price: number
  img?: string
}

interface CurrentBook {
  id: number
  title: string
  description: string
  price: number
  img?: string
  author: string
}

export type { IAuthor, IBook, CurrentBook }