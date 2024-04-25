import {Component, OnInit} from '@angular/core';
import {RouterLink} from "@angular/router";
import {ProductsListService} from "../products-list.service";
import {Observable} from "rxjs";
import {Product} from "../models";
import {AsyncPipe} from "@angular/common";

@Component({
  selector: 'app-products-list',
  standalone: true,
  imports: [
    RouterLink,
    AsyncPipe
  ],
  templateUrl: './products-list.component.html',
  styleUrl: './products-list.component.css'
})
export class ProductsListComponent implements OnInit{

  products: Observable<Product[]> = new Observable<Product[]>();
  constructor(private productservice: ProductsListService) {
    this.products = new Observable<Product[]>();
  }

  ngOnInit() {
    console.log("inside ng")
    this.reloadData()
  }

  reloadData() {
    this.products = this.productservice.getProductList()
  }

  addToCart() {

  }
}
