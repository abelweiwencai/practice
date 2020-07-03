import { Component, OnInit } from '@angular/core';
import { Hero } from '../model/hero/hero';

import { HeroService} from '../service/hero/hero.service';
import { MessageService } from '../service/message/message.service';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})
export class HeroesComponent implements OnInit {
  heroes: Hero[];
  selectedHero: Hero;
  onSelect(hero: Hero): void {
    this.messageService.add(`you have selected hero: id=${hero.id}, name=${hero.name}`);
    this.selectedHero = hero;
  }

  constructor(private heroService: HeroService, private messageService: MessageService) { }
  getHeroes(): void {
    this.heroService.getHeroes().subscribe(heroes => this.heroes = heroes);
  }

  ngOnInit(): void {
    this.getHeroes();
  }

}
