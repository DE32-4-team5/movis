package com.samdul.movis.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.samdul.movis.entity.MovisEntity;
import com.samdul.movis.service.MovisService;

@RestController
public class MovisController {
    @Autowired
    private MovisService movisService;

    @GetMapping("/movies/{nm}")
    public MovisEntity find(@PathVariable String nm) {
        System.out.println("[Controller] find by name");
        MovisEntity result = movisService.findByNm(nm);
        return result;
    }

    @GetMapping("/genres/{gn}")
    public MovisEntity findByGenre(@PathVariable String gn) {
        System.out.println("[Controller] find by genre");
        MovisEntity result = movisService.findByGn(gn);
        return result;
    }

    @GetMapping("/people/{pn}")
    public MovisEntity findByPerson(@PathVariable String pn) {
        System.out.println("[Controller] find by person");
        MovisEntity result = movisService.findByPn(pn);
        return result;
    }
}
