<template>
  <card>
    <div class="pa-2">
      <v-select
        v-model="selectedSource"
        :label="$t('import_data.select_source.title')"
        outlined
        :items="sources"
        item-value="identifier"
        item-text="name"
        :hide-details="true"
      >
        <template
          v-for="slotName in ['item', 'selection']"
          :slot="slotName"
          slot-scope="data"
        >
          <div v-if="data.item" :key="slotName" class="d-flex align-center">
            <adaptive-wrapper>
              <v-img
                :src="data.item.logo"
                :width="30"
                :height="30"
                max-height="30px"
                max-width="30px"
                position="center left"
                contain
              />
            </adaptive-wrapper>
            <div class="pl-3">{{ data.item.name }}</div>
          </div>
        </template>
      </v-select>

      <div v-if="form" class="mt-8">
        <component :is="form" />
      </div>
    </div>
  </card>
</template>
<script lang="ts">
import { computed, defineComponent, ref } from '@vue/composition-api';
import AdaptiveWrapper from '@/components/display/AdaptiveWrapper.vue';
import BisqImport from '@/components/import/Bisq.vue';
import BlockFiImport from '@/components/import/BlockFiImport.vue';
import CointrackingImport from '@/components/import/CointrackingImport.vue';
import CryptoComImport from '@/components/import/CryptoComImport.vue';
import NexoImport from '@/components/import/NexoImport.vue';
import ShapeshiftImport from '@/components/import/ShapeshiftImport.vue';
import UpholdImport from '@/components/import/UpholdImport.vue';
import i18n from '@/i18n';

const sources = () =>
  computed(() => {
    const sources = [
      {
        identifier: 'cointracking.info',
        name: i18n.t('import_data.cointracking.name').toString(),
        logo: require('@/assets/images/cointracking.svg'),
        form: 'cointracking-import'
      },
      {
        identifier: 'cryptocom',
        name: i18n.t('import_data.cryptocom.name').toString(),
        logo: require('@/assets/images/crypto_com.svg'),
        form: 'crypto-com-import'
      },
      {
        identifier: 'blockfi',
        name: i18n.t('import_data.blockfi.name').toString(),
        logo: require('@/assets/images/blockfi.svg'),
        form: 'block-fi-import'
      },
      {
        identifier: 'nexo',
        name: i18n.t('import_data.nexo.name').toString(),
        logo: require('@/assets/images/nexo.svg'),
        form: 'nexo-import'
      },
      {
        identifier: 'shapeshift-trades',
        name: i18n.t('import_data.shapeshift.name').toString(),
        logo: require('@/assets/images/shapeshift.svg'),
        form: 'shapeshift-import'
      },
      {
        identifier: 'uphold',
        name: i18n.t('import_data.uphold.name').toString(),
        logo: require('@/assets/images/uphold.svg'),
        form: 'uphold-import'
      },
      {
        identifier: 'bisq',
        name: i18n.t('import_data.bisq.name'),
        logo: require('@/assets/images/bisq.svg'),
        form: 'bisq-import'
      }
    ];

    return sources;
  });

export default defineComponent({
  name: 'GroupedImport',
  components: {
    AdaptiveWrapper,
    UpholdImport,
    ShapeshiftImport,
    NexoImport,
    BlockFiImport,
    CryptoComImport,
    CointrackingImport,
    BisqImport
  },
  setup() {
    const selectedSource = ref<string>('');

    const form = computed(() => {
      return sources().value.find(
        source => source.identifier === selectedSource.value
      )?.form;
    });

    return {
      selectedSource,
      form,
      sources: sources()
    };
  }
});
</script>
