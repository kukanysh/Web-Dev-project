import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Category, Product } from './models';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AppService {
  BASE_URL = 'http://127.0.0.1:8000'

  constructor(private http: HttpClient) { }

  getCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(
      `${this.BASE_URL}/api/categories/`
    )
  }

  getCategoryProducts(id: number): Observable<Product[]> {
    return this.http.get<Product[]>
    (`${this.BASE_URL}/api/categories/${id}/products`);
  }





}


