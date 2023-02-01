from django.test import TestCase
from .models import Sekolah

class SekolahTestCase(TestCase):
    def setUp(self):
        Sekolah.objects.create(NPSN="202682xx", nama="smkn2 sukabumi", status="Negeri")
        
        def test_sekolah_cek_nama(self):
            """cek nama sekolah"""
            smkn2= Sekolah.objects.get(nama="smkn2 sukabumi")
            self.assertEqual(smkn2.nama, "smkn2 sukabumi")
            
   
    def test_create(self):
# create
        instance = Sekolah(nama='smkn2 sukabumi', status= 'Negeri')
        instance.save()
# update
        instance.nama= 'smkn2 sukabumi'
        instance.save()
        
        update_instance = Sekolah.objects.get(id=instance.id)
        self.assertEqual(update_instance.nama, 'smkn2 sukabumi')
        
        

    def test_read(self):
        instance = Sekolah(nama='smkn2 sukabumi',)
        instance.save()
        retrieved_instance = Sekolah.objects.get(id=instance.id)
        self.assertEqual(retrieved_instance.nama, 'smkn2 sukabumi')
        
    def test_delete(self):
        instance=Sekolah.objects.get(id= 1).delete()[0]
        self.assertEqual(instance, 1)
            
