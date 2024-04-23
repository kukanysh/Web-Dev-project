import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from '@angular/router';
import {TopBarComponent} from "./top-bar/top-bar.component";
import {BodyComponent} from "./body/body.component";
import {BottomBarComponent} from "./bottom-bar/bottom-bar.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, TopBarComponent, BodyComponent, BottomBarComponent, RouterLink],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
