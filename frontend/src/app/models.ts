export interface Category {
  id: number;
  name: string;
}


export interface Product {
  id: number;
  name: string;
  description: string;
  image: string;
  brand: string;
  price: number;
  rating: number;
  category: Category

}
