import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Products } from '../models/products.model';
const baseUrl = 'http://localhost:8000/api/products';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  constructor(private http: HttpClient) { }
  getAll(): Observable<Products[]> {
    return this.http.get<Products[]>(baseUrl);
  }
}
