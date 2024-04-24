import { Routes } from '@angular/router';
import { CartComponent} from "./cart/cart.component";
import { HomeComponent} from "./home/home.component";
import { ProductsListComponent} from "./products-list/products-list.component";
import { OrdersComponent} from "./orders/orders.component";
import {ProductInfoComponent} from "./product-info/product-info.component";

export const routes: Routes = [
  {'path': '', component: HomeComponent},
  {'path': 'orders', component: OrdersComponent},
  {'path': 'products-list', component: ProductsListComponent},
  {'path': 'products-list', children:[
      {'path': 'product-info', component: ProductInfoComponent},
]},
  {'path': 'cart', component: CartComponent},



];
