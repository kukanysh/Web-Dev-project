export interface Category {
  id: number;
  name: string;
  description: string;
}

export interface Product {
  id: number;
  name: string;
  description: string;
  image_url: string;
  categoryId: number;
  price: BigInteger;
}



export interface Order {
  id: number;
  product: Product;
}

