import { Component, OnInit  } from '@angular/core';
import {RouterLink} from "@angular/router";
import { Category } from '../models';
import { AppService } from '../app.service'
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-products-list',
  standalone: true,
  imports: [
    RouterLink,
    RouterModule,
    CommonModule,
  ],
  templateUrl: './products-list.component.html',
  styleUrl: './products-list.component.css'
})
export class ProductsListComponent implements OnInit {

  products: Category[] = [];
  loaded: boolean;
  constructor(private appservice: AppService) {
    this.loaded = false;
  }

  ngOnInit(): void {
    this.getCategories();
  }

  addToCart() {
    // Implement your logic to add the item to the cart here
    console.log('Item added to cart');
    // You can also call a service method to add the item to the cart
  }

  getCategories():void{
    this.appservice.getCategories().subscribe((data) => {
      this.products = data;
      this.loaded = true;
    });
  }


}
