import { Component } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Task {
  id: number;
  name: string;
  description: string;
  issued: string;
  due: string;
}

@Injectable({
  providedIn: 'root'
})
@Component({
  selector: 'app-task-service',
  standalone: true,
  imports: [],
  templateUrl: './task-service.component.html',
  styleUrl: './task-service.component.css'
})
export class TaskServiceComponent {
  private apiUrl = 'http://localhost:8000/tasks';

  constructor(private http: HttpClient) {}

  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(this.apiUrl);
  }

  addTask(task: Task): Observable<Task> {
    return this.http.post<Task>(this.apiUrl, task);
  }
}
