import { Component } from '@angular/core';
import {RouterLink} from '@angular/router';

@Component({
  selector: 'app-home-hub',
  standalone: true,
  imports: [
    RouterLink
  ],
  templateUrl: './home-hub.component.html',
  styleUrl: './home-hub.component.css'
})
export class HomeHubComponent {

}
