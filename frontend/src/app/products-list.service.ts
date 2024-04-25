import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ProductsListService {

  private productListUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  getProductList(): Observable<any>{
    return this.http.get(`${this.productListUrl}`)
  }

}
