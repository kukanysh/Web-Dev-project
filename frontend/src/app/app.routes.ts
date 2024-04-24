import { Routes } from '@angular/router';
import { CartComponent} from "./cart/cart.component";
import { HomeComponent} from "./home/home.component";
import { ProductsComponent} from "./products/products.component";
import { OrdersComponent} from "./orders/orders.component";

export const routes: Routes = [
  {'path': '', component: HomeComponent},
  {'path': 'orders', component: OrdersComponent},
  {'path': 'products', component: ProductsComponent},
  {'path': 'cart', component: CartComponent},



];
