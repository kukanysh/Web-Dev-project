import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CartComponent} from "./cart/cart.component";

const routes: Routes = [
  { path: 'cart', component: CartComponent },
  { path: '', redirectTo: 'cart', pathMatch: 'full' }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
