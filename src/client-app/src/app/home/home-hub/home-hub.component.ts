import {RouterLink} from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../authentication/auth.service';
import {AuthGuard} from '../../authentication/auth.guard';
import {TaskGraphEditorComponent} from '../task-graph-editor/task-graph-editor.component';

@Component({
  selector: 'app-home-hub',
  standalone: true,
  imports: [
    RouterLink,
    TaskGraphEditorComponent
  ],
  templateUrl: './home-hub.component.html',
  styleUrl: './home-hub.component.css'
})
export class HomeHubComponent implements OnInit{
  constructor(
    private authService: AuthService,
    private authGuard: AuthGuard
  ) {}

  logout(): void {
    this.authService.logout();
  }

  ngOnInit() {
    this.authGuard.canActivate().subscribe()
    // TODO figure out how to get rid of subscribe()
  }
}
